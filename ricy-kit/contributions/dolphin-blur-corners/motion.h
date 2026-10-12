// SPDX-License-Identifier: MIT
#pragma once
#include <QAbstractButton>
#include <QApplication>
#include <QEnterEvent>
#include <QGraphicsEffect>
#include <QHoverEvent>
#include <QItemSelectionModel>
#include <QLineEdit>
#include <QListView>
#include <QMouseEvent>
#include <QPainter>
#include <QPersistentModelIndex>
#include <QPointer>
#include <QStyle>
#include <QTabBar>
#include <QToolBar>
#include <QTimer>
#include <QVariantAnimation>
#include <KConfigGroup>
#include <KSharedConfig>

namespace {
// Existing grounding cadence, local to this Qt adaptation; not new tokens.
constexpr int MotionFast = 100;
constexpr int MotionHover = 140;
constexpr int MotionState = 160;
constexpr int MotionNormal = 200;

class ChromeMotion final : public QGraphicsEffect {
public:
    explicit ChromeMotion(QWidget *target, QListView *places = nullptr)
        : QGraphicsEffect(target), m_target(target), m_places(places), m_animation(this) {
        setObjectName(QStringLiteral("ricyChromeMotion"));
        setEnabled(false); // Native direct painting when stable; no effect capture loop.
        m_animation.setObjectName(QStringLiteral("ricyChromeTransition"));
        m_animation.setEasingCurve(QEasingCurve::OutCubic);
        target->installEventFilter(this);
        if (places) places->installEventFilter(this);
        connect(&m_animation, &QVariantAnimation::valueChanged, this, [this](const QVariant &value) {
            m_mix = value.toReal();
            update(); // Only this control/Places viewport; never the file view.
        });
        connect(&m_animation, &QVariantAnimation::finished, this, [this] {
            m_from = QPixmap();
            m_mix = 1;
            setEnabled(false);
            captureNative();
        });
        if (auto *editor = qobject_cast<QLineEdit *>(target))
            connect(editor, &QLineEdit::textChanged, this, [this] {
                settle();
                m_presented = QPixmap(); // Typed/path content is never animated.
            });
        if (auto *tabs = qobject_cast<QTabBar *>(target))
            connect(tabs, &QTabBar::currentChanged, this, [this] { begin(MotionState); });
        if (auto *button = qobject_cast<QAbstractButton *>(target))
            connect(button, &QAbstractButton::toggled, this, [this] { begin(MotionState); });
        bindSelection();
    }
    bool running() const { return m_animation.state() == QAbstractAnimation::Running; }
    qreal progress() const { return m_mix; }
    int duration() const { return m_animation.duration(); }
    QRectF boundingRectFor(const QRectF &rect) const override { return rect; }

protected:
    void draw(QPainter *painter) override {
        QPoint offset;
        const QPixmap final = sourcePixmap(Qt::LogicalCoordinates, &offset, NoPad);
        if (final.isNull()) { drawSource(painter); return; }
        if (!running() || m_from.size() != final.size() ||
            m_from.devicePixelRatio() != final.devicePixelRatio() || offset != m_offset) {
            m_presented = final;
        } else {
            // Premultiplied additive blending keeps shared opaque text/background
            // opaque. SourceOver twice would dim the whole control mid-transition.
            QPixmap frame(final.size());
            frame.setDevicePixelRatio(final.devicePixelRatio());
            frame.fill(Qt::transparent);
            QPainter blend(&frame);
            blend.setOpacity(1 - m_mix);
            blend.drawPixmap(0, 0, m_from);
            blend.setCompositionMode(QPainter::CompositionMode_Plus);
            blend.setOpacity(m_mix);
            blend.drawPixmap(0, 0, final);
            blend.end();
            m_presented = frame;
        }
        m_offset = offset;
        painter->drawPixmap(offset, m_presented);
    }
    void sourceChanged(ChangeFlags flags) override {
        if (flags.testFlag(SourceBoundingRectChanged) || flags.testFlag(SourceDetached)) {
            settle();
            m_presented = QPixmap();
        }
        QGraphicsEffect::sourceChanged(flags);
    }
    bool eventFilter(QObject *object, QEvent *event) override {
        if (!m_target) return false;
        switch (event->type()) {
        case QEvent::Show:
            bindSelection();
            // Prime a native stable frame after show, once, without idle polling.
            QTimer::singleShot(0, this, [this] {
                if (m_target && !running() && m_target->isVisible())
                    captureNative();
            });
            break;
        case QEvent::Resize:
        case QEvent::Hide:
        case QEvent::EnabledChange:
        case QEvent::StyleChange:
        case QEvent::PaletteChange:
        case QEvent::FontChange:
            settle();
            break;
        case QEvent::FocusIn:
        case QEvent::FocusOut:
            begin(MotionFast);
            break;
        case QEvent::Enter:
        case QEvent::Leave:
            if (qobject_cast<QAbstractButton *>(m_target)) begin(MotionHover);
            else if (qobject_cast<QTabBar *>(m_target) || m_places) {
                const QPoint position = event->type() == QEvent::Enter
                    ? static_cast<QEnterEvent *>(event)->position().toPoint() : QPoint(-1,-1);
                hover(position);
            }
            break;
        case QEvent::MouseMove:
            hover(static_cast<QMouseEvent *>(event)->position().toPoint());
            break;
        case QEvent::HoverMove:
            hover(static_cast<QHoverEvent *>(event)->position().toPoint());
            break;
        case QEvent::MouseButtonPress:
        case QEvent::MouseButtonRelease:
            if (qobject_cast<QAbstractButton *>(m_target)) begin(MotionFast);
            break;
        default:
            break;
        }
        Q_UNUSED(object);
        return false; // Native events, selection, actions and hit areas stay upstream.
    }

private:
    void captureNative() {
        // Render the native control without copying its parent's backing into
        // transparent rounded corners. Only called with the effect disabled.
        if (!m_target || m_target->size().isEmpty()) return;
        QPixmap frame(m_target->size() * m_target->devicePixelRatioF());
        frame.setDevicePixelRatio(m_target->devicePixelRatioF());
        frame.fill(Qt::transparent);
        m_target->render(&frame, QPoint(), QRegion(), QWidget::DrawChildren);
        m_presented = frame;
        m_offset = QPoint();
    }
    int effectiveDuration(int reference) const {
        if (!m_target || !m_target->isEnabled() || !m_target->isVisible()) return 0;
        const QStyle *style = m_target->style();
        if (!style->styleHint(QStyle::SH_Widget_Animate, nullptr, m_target)) return 0;
        const int native = style->styleHint(QStyle::SH_Widget_Animation_Duration, nullptr, m_target);
        if (native <= 0) return 0;
        // A zero KDE animation factor is an explicit disable. A positive KWin
        // factor is not used as a widget clock. No Noctalia runtime dependency.
        const auto globals = KSharedConfig::openConfig(QStringLiteral("kdeglobals"), KConfig::NoGlobals);
        if (KConfigGroup(globals, "KDE").readEntry("AnimationDurationFactor", 1.0) <= 0) return 0;
        return qBound(1, qRound(reference * qreal(native) / MotionNormal), 400);
    }
    void begin(int reference) {
        const int duration = effectiveDuration(reference);
        if (!duration) { settle(); return; }
        if (m_presented.isNull()) captureNative();
        if (m_presented.isNull()) { settle(); return; }
        // An interrupted transition starts at the last actually painted frame.
        m_animation.stop();
        m_from = m_presented;
        m_mix = 0;
        m_animation.setDuration(duration);
        m_animation.setStartValue(0.0);
        m_animation.setEndValue(1.0);
        setEnabled(true);
        m_animation.start();
    }
    void settle() {
        const bool changed = running() || !m_from.isNull() || m_mix != 1;
        m_animation.stop();
        m_from = QPixmap();
        m_mix = 1;
        setEnabled(false);
        // Qt already schedules native geometry/style paints. Do not feed an
        // idle source-bounds notification back into another effect repaint.
        if (changed) update();
    }
    void hover(const QPoint &position) {
        if (auto *tabs = qobject_cast<QTabBar *>(m_target)) {
            const int index = tabs->tabAt(position);
            if (index != m_hoveredTab) { m_hoveredTab = index; begin(MotionHover); }
        } else if (m_places) {
            const QPersistentModelIndex index(m_places->indexAt(position));
            if (index != m_hoveredPlace) { m_hoveredPlace = index; begin(MotionHover); }
        }
    }
    void bindSelection() {
        if (m_places && m_model != m_places->model()) {
            for (const auto &connection : m_modelConnections) QObject::disconnect(connection);
            m_modelConnections.clear();
            m_model = m_places->model();
            if (m_model) {
                const auto nativeContentChanged = [this] {
                    // Device/status/model changes are immediate native content,
                    // never a crossfade of stale storage/state information.
                    settle();
                    m_presented = QPixmap();
                };
                m_modelConnections.append(connect(m_model, &QAbstractItemModel::dataChanged, this, nativeContentChanged));
                m_modelConnections.append(connect(m_model, &QAbstractItemModel::modelReset, this, nativeContentChanged));
                m_modelConnections.append(connect(m_model, &QAbstractItemModel::rowsInserted, this, nativeContentChanged));
                m_modelConnections.append(connect(m_model, &QAbstractItemModel::rowsRemoved, this, nativeContentChanged));
                m_modelConnections.append(connect(m_model, &QAbstractItemModel::layoutChanged, this, nativeContentChanged));
            }
        }
        if (!m_places || m_selection == m_places->selectionModel()) return;
        QObject::disconnect(m_selectionConnection);
        m_selection = m_places->selectionModel();
        if (m_selection)
            m_selectionConnection = connect(m_selection, &QItemSelectionModel::selectionChanged,
                this, [this] { begin(MotionState); });
    }
    QPointer<QWidget> m_target;
    QPointer<QListView> m_places;
    QPointer<QItemSelectionModel> m_selection;
    QPointer<QAbstractItemModel> m_model;
    QList<QMetaObject::Connection> m_modelConnections;
    QMetaObject::Connection m_selectionConnection;
    QVariantAnimation m_animation;
    QPixmap m_from, m_presented;
    QPoint m_offset;
    QPersistentModelIndex m_hoveredPlace;
    int m_hoveredTab = -1;
    qreal m_mix = 1;
};

void installChromeMotion(QWidget *widget) {
    if (!widget) return;
    // Do not nest effects (for example a path editor and its clear button).
    for (auto *parent = widget->parentWidget(); parent; parent = parent->parentWidget())
        if (parent->graphicsEffect() && parent->graphicsEffect()->objectName() == QStringLiteral("ricyChromeMotion")) return;
    if (qobject_cast<QLineEdit *>(widget))
        for (auto *child : widget->findChildren<QWidget *>())
            if (child->graphicsEffect() && child->graphicsEffect()->objectName() == QStringLiteral("ricyChromeMotion"))
                child->setGraphicsEffect(nullptr);
    if (widget->inherits("KFilePlacesView")) {
        if (auto *places = qobject_cast<QListView *>(widget))
            if (!places->viewport()->graphicsEffect())
                places->viewport()->setGraphicsEffect(new ChromeMotion(places->viewport(), places));
        return;
    }
    bool eligible = qobject_cast<QTabBar *>(widget);
    for (auto *parent = widget->parentWidget(); parent && !eligible; parent = parent->parentWidget())
        if (qobject_cast<QToolBar *>(parent) || parent->inherits("KUrlNavigator"))
            eligible = qobject_cast<QAbstractButton *>(widget) || qobject_cast<QLineEdit *>(widget);
    if (eligible && !widget->graphicsEffect()) widget->setGraphicsEffect(new ChromeMotion(widget));
}
} // namespace
