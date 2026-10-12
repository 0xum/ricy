// SPDX-License-Identifier: MIT
#include <QGenericPlugin>
#include <QApplication>
#include <QWidget>
#include <QEvent>
#include <QTimer>
#include <QProxyStyle>
#include <QStyleFactory>
#include <QStyleOptionViewItem>
#include <QStyleOptionHeader>
#include <QFont>
#include <QPainter>
#include <QAbstractItemView>
#include <QAbstractItemDelegate>
#include <QGraphicsWidget>
#include <QGraphicsEffect>
#include <QPointer>
#include <QTabBar>
#include <QTabWidget>
#include <QToolButton>
#include <QGraphicsView>
#include <QGraphicsScene>
#include <QPainterPath>
#include <QListView>
#include <QAbstractButton>
#include <QComboBox>
#include <QLayout>
#include <QMenu>
#include <QDockWidget>
#include <QSplitterHandle>
#include <QMouseEvent>

namespace {
struct PlacesPaint { QString text; int iconSize; };

thread_local const QRectF *rowPaint = nullptr;
thread_local int *rowDepth = nullptr;
thread_local bool *rowFocus = nullptr;
thread_local const QRectF *headerPaint = nullptr;
thread_local int lastHeaderSection = -1;
bool fileViewport(const QWidget *widget) {
    for (const QWidget *parent = widget; parent; parent = parent->parentWidget())
        if (parent->inherits("KItemListContainerViewport")) return true;
    return false;
}
void chip(QPainter *painter, QRectF rect, QColor fill, QColor outline = Qt::transparent) {
    if (rect.isEmpty()) return;
    painter->save();
    painter->setRenderHint(QPainter::Antialiasing);
    painter->setPen(outline.alpha() ? QPen(outline, 1) : QPen(Qt::NoPen));
    painter->setBrush(fill);
    const qreal radius = qMin<qreal>(6, rect.height()/2);
    painter->drawRoundedRect(rect, radius, radius);
    painter->restore();
}
class ChipStyle : public QProxyStyle {
public:
    explicit ChipStyle(QStyle *base) : QProxyStyle(base) {}
    int pixelMetric(PixelMetric metric, const QStyleOption *option = nullptr,
                    const QWidget *widget = nullptr) const override {
        const auto *tabs = qobject_cast<const QTabBar *>(widget);
        if (metric == PM_TabBarScrollButtonWidth && tabs &&
            (tabs->shape() == QTabBar::RoundedNorth || tabs->shape() == QTabBar::RoundedSouth))
            return 24;
        return QProxyStyle::pixelMetric(metric, option, widget);
    }
    QRect subElementRect(SubElement element, const QStyleOption *option,
                         const QWidget *widget = nullptr) const override {
        if (element == SE_TabWidgetTabBar && option) {
            const auto *container = qobject_cast<const QTabWidget *>(widget);
            if (container && (container->tabPosition() == QTabWidget::North ||
                              container->tabPosition() == QTabWidget::South)) {
                // Reserve the shell's trailing gutter in the actual tab-bar
                // allocation, including when every tab fits without arrows.
                QRect available = option->rect;
                if (container->layoutDirection() == Qt::RightToLeft)
                    available.adjust(8,0,0,0);
                else
                    available.adjust(0,0,-8,0);
                return QProxyStyle::subElementRect(element, option, widget).intersected(available);
            }
        }
        const auto *tabs = qobject_cast<const QTabBar *>(widget);
        if (tabs && option && (tabs->shape() == QTabBar::RoundedNorth ||
                              tabs->shape() == QTabBar::RoundedSouth) &&
            (element == SE_TabBarTearIndicatorLeft || element == SE_TabBarTearIndicatorRight)) {
            QRect rect = QProxyStyle::subElementRect(element, option, widget);
            if (!rect.isEmpty() && rect.width() < 4) {
                const bool left = (element == SE_TabBarTearIndicatorLeft) !=
                                  (tabs->layoutDirection() == Qt::RightToLeft);
                if (left) rect.setWidth(4);
                else rect.setLeft(rect.right()-3);
            }
            return rect;
        }
        if (tabs && option && (tabs->shape() == QTabBar::RoundedNorth ||
                              tabs->shape() == QTabBar::RoundedSouth) &&
            (element == SE_TabBarScrollLeftButton || element == SE_TabBarScrollRightButton)) {
            // Qt uses these rectangles for both clipping and layout. The larger
            // leading rectangle reserves two 24px buttons, an 8px gap and an 8px edge inset;
            // PM_TabBarScrollButtonWidth retains the native button hit areas.
            const QRect area = option->rect;
            const QRect rect = element == SE_TabBarScrollLeftButton
                ? QRect(area.right() - 63, area.top(), 64, area.height())
                : QRect(area.right() - 31, area.top(), 24, area.height());
            return QStyle::visualRect(tabs->layoutDirection(), area, rect);
        }
        return QProxyStyle::subElementRect(element, option, widget);
    }
    void drawPrimitive(PrimitiveElement element, const QStyleOption *option,
                       QPainter *painter, const QWidget *widget = nullptr) const override {
        if (qobject_cast<const QTabBar *>(widget) &&
            (element == PE_IndicatorTabTearLeft || element == PE_IndicatorTabTearRight)) {
            // Keep Qt's native overflow visibility/placement, using the existing
            // accent and a 4px capsule instead of Kvantum's thin blue line.
            const QRectF area(option->rect);
            const qreal width = qMin<qreal>(4, area.width());
            const QRectF line(area.center().x()-width/2, area.top()+3,
                              width, qMax<qreal>(0,area.height()-6));
            painter->save();
            painter->setRenderHint(QPainter::Antialiasing);
            painter->setPen(Qt::NoPen);
            painter->setBrush(QColor("#cba6f7"));
            painter->drawRoundedRect(line,width/2,width/2);
            painter->restore();
            return;
        }
        if (widget && QByteArray(widget->metaObject()->className()).contains("KUrlNavigator") &&
            (element == PE_IndicatorArrowRight || element == PE_IndicatorArrowLeft || element == PE_IndicatorArrowDown)) {
            painter->save();
            painter->setRenderHint(QPainter::Antialiasing);
            painter->setPen(QPen(option->palette.color(QPalette::WindowText), 1.5,
                                 Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
            painter->setBrush(Qt::NoBrush);
            const QPointF center = QRectF(option->rect).center();
            QPainterPath arrow;
            if (element == PE_IndicatorArrowDown) {
                arrow.moveTo(center+QPointF(-3,-1.5));
                arrow.lineTo(center+QPointF(0,1.5));
                arrow.lineTo(center+QPointF(3,-1.5));
            } else {
                const int direction = element == PE_IndicatorArrowLeft ? -1 : 1;
                arrow.moveTo(center+QPointF(-1.5*direction,-3));
                arrow.lineTo(center+QPointF(1.5*direction,0));
                arrow.lineTo(center+QPointF(-1.5*direction,3));
            }
            painter->drawPath(arrow);
            painter->restore();
            return;
        }
        if (element == PE_PanelButtonCommand && widget &&
            QByteArray(widget->metaObject()->className()).contains("KUrlNavigator")) {
            QColor hover("#977dba"); hover.setAlpha(65);
            chip(painter, QRectF(option->rect).adjusted(1,2,-1,-2), hover);
            return;
        }
        const auto *viewOption = qstyleoption_cast<const QStyleOptionViewItem *>(option);
        const QWidget *candidate = widget ? widget : (viewOption ? viewOption->widget : nullptr);
        if (!candidate) candidate = dynamic_cast<QWidget *>(painter->device());
        const QAbstractItemView *placesView = nullptr;
        for (const QWidget *parent = candidate; parent; parent = parent->parentWidget()) {
            if (parent->inherits("KFilePlacesView")) {
                placesView = qobject_cast<const QAbstractItemView *>(parent);
                break;
            }
        }
        PlacesPaint context;
        const PlacesPaint *placesPaint = nullptr;
        if (placesView) {
            QModelIndex index = viewOption ? viewOption->index : QModelIndex();
            if (!index.isValid()) index = placesView->indexAt(option->rect.center());
            if (index.isValid()) {
                context = {index.data(Qt::DisplayRole).toString(), placesView->iconSize().width()};
                placesPaint = &context;
            }
        }
        const bool places = placesPaint != nullptr;
        const bool files = rowPaint || fileViewport(widget);
        if (element == PE_IndicatorBranch) {
            if (rowDepth && (option->state & State_Item)) {
                // Native branch slots advance one row height per nesting level.
                const int offset = option->direction == Qt::RightToLeft && rowPaint
                    ? int(rowPaint->width()) - option->rect.right() - 1
                    : option->rect.left();
                *rowDepth = qMax(0, qRound(qreal(offset - 20) / qMax(1, option->rect.height())));
            }
            // State_Children comes from Dolphin's model: ordinary files get no arrow.
            if (!(option->state & State_Children)) return;
            painter->save();
            painter->setRenderHint(QPainter::Antialiasing);
            QPen pen(QColor("#a6adc8"), 1.5, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin);
            painter->setPen(pen); painter->setBrush(Qt::NoBrush);
            QPointF center = QRectF(option->rect).center();
            const int branchOffset = option->direction == Qt::RightToLeft && rowPaint
                ? int(rowPaint->width()) - option->rect.right() - 1 : option->rect.left();
            if (branchOffset > 20 + option->rect.height()/2)
                center.rx() += option->direction == Qt::RightToLeft ? -4 : 4;
            QPainterPath path;
            if (option->state & State_Open) {
                path.moveTo(center + QPointF(-3,-1.5));
                path.lineTo(center + QPointF(0,1.5));
                path.lineTo(center + QPointF(3,-1.5));
            } else {
                const qreal direction = option->direction == Qt::RightToLeft ? -1 : 1;
                path.moveTo(center + QPointF(-1.5*direction,-3));
                path.lineTo(center + QPointF(1.5*direction,0));
                path.lineTo(center + QPointF(-1.5*direction,3));
            }
            painter->drawPath(path); painter->restore(); return;
        }
        if ((places || files) && element == PE_PanelItemViewItem) {
            const bool selected = option->state & State_Selected;
            const bool hovered = option->state & State_MouseOver;
            if (!places && !selected && !hovered) return;
            QRectF rect = (rowPaint ? *rowPaint : QRectF(option->rect)).adjusted(3, 2, -3, -2);
            if (places) {
                rect = QRectF(option->rect);
                // Search-result treatment: only hover/selection have a backing.
                if (!selected && !hovered) return;
                QColor fill(selected ? "#cba6f7" : "#977dba");
                if (!selected) fill.setAlpha(65);
                painter->save();
                painter->setRenderHint(QPainter::Antialiasing);
                painter->setPen(Qt::NoPen);
                painter->setBrush(fill);
                painter->drawRoundedRect(rect, 8, 8);
                painter->restore();
                return;
            }
            QColor fill("#977dba");
            fill.setAlpha(selected ? 170 : 95);
            if (selected && hovered) fill.setAlpha(195);
            chip(painter, rect, fill);
            return;
        }
        if ((places || files) && element == PE_FrameFocusRect) {
            if (rowFocus) { *rowFocus = true; return; }
            chip(painter, (rowPaint ? *rowPaint : QRectF(option->rect)).adjusted(3, 2, -3, -2), Qt::transparent, QColor("#cba6f7"));
            return;
        }
        QProxyStyle::drawPrimitive(element, option, painter, widget);
    }
    QRectF headerChipRect(const QStyleOptionHeader *header, const QWidget *widget) const {
        // Shared edges: previous column ends at boundary+3, next begins at
        // boundary+9. This leaves a consistent 6px gap, preserving Name's arrow.
        QRectF rect = QRectF(header->rect).adjusted(header->section == 0 ? -8 : 9, 3, 3, -3);
        const bool trailing = header->section == lastHeaderSection
            || header->position == QStyleOptionHeader::End;
        if (headerPaint) {
            const QRectF inner = headerPaint->adjusted(5,3,-5,-3);
            if (trailing) rect.setRight(inner.right());
            rect = rect.intersected(inner);
        }
        if (header->section > 0 && header->sortIndicator != QStyleOptionHeader::None) {
            const QRect arrow = subElementRect(SE_HeaderArrow, header, widget);
            if (arrow.center().x() < header->rect.center().x())
                rect.setLeft(qMax(rect.left(), qreal(arrow.right() + 4)));
            else
                rect.setRight(qMin(rect.right(), qreal(arrow.left() - 4)));
        }
        return rect;
    }
    void drawControl(ControlElement element, const QStyleOption *option,
                     QPainter *painter, const QWidget *widget = nullptr) const override {
        if (element == CE_RubberBand) {
            // Preserve the native drag rectangle and animation opacity while
            // matching the medium-radius translucent selection treatment.
            QColor fill("#977dba"); fill.setAlpha(65);
            QColor outline("#cba6f7"); outline.setAlpha(150);
            chip(painter, QRectF(option->rect).adjusted(0.5,0.5,-0.5,-0.5), fill, outline);
            return;
        }
        if (element == CE_Header && (headerPaint || fileViewport(widget))) {
            const auto *header = qstyleoption_cast<const QStyleOptionHeader *>(option);
            if (!header) return;
            // Dolphin paints the trailing padding immediately before its last label.
            if (header->text.isEmpty() && header->position == QStyleOptionHeader::End)
                lastHeaderSection = header->section - 1;
            if (option->state & State_MouseOver) {
                QColor fill("#977dba"); fill.setAlpha(65);
                const QRectF hover = headerChipRect(header, widget);
                chip(painter, hover, fill);
            }
            // The common rounded header backing is drawn once by HeaderChip.
            // Keep native text layout, sorting arrows, resizing and reordering.
            QStyleOptionHeader label(*header);
            label.rect = subElementRect(SE_HeaderLabel, header, widget);
            if (!header->text.isEmpty()) {
                const QRectF capsule = headerChipRect(header, widget);
                label.rect.setLeft(qMax(label.rect.left(), int(capsule.left()) + 8));
                label.rect.setRight(qMin(label.rect.right(), int(capsule.right()) - 8));
            }
            QProxyStyle::drawControl(CE_HeaderLabel, &label, painter, widget);
            if (header->sortIndicator != QStyleOptionHeader::None) {
                QStyleOptionHeader arrow(*header);
                arrow.rect = subElementRect(SE_HeaderArrow, header, widget);
                QProxyStyle::drawPrimitive(PE_IndicatorHeaderArrow, &arrow, painter, widget);
            }
            return;
        }
        QProxyStyle::drawControl(element, option, painter, widget);
    }
};

// Keep KFilePlacesView's default delegate alive and installed. A column-only
// paint adapter forwards native geometry, device controls, help and editor
// events. Unlike replacing/deleting the default delegate, this leaves KIO's
// private delegate pointer, timers and existing signal connections intact.
class PlacesResultPaint : public QAbstractItemDelegate {
public:
    PlacesResultPaint(QAbstractItemDelegate *native, QObject *parent)
        : QAbstractItemDelegate(parent), m_native(native) {}
    void paint(QPainter *painter, const QStyleOptionViewItem &option,
               const QModelIndex &index) const override {
        if (!m_native) return;
        QStyleOptionViewItem styled(option);
        // KIO's text rectangle starts at a fixed local x, while the icon
        // includes rect.left(). Normalize the origin to retain its 6px gap
        // even with QListView spacing and viewport padding.
        painter->save();
        painter->translate(option.rect.left(), 0);
        styled.rect.moveLeft(0);
        styled.font.setWeight(QFont::DemiBold);
        styled.fontMetrics = QFontMetrics(styled.font);
        painter->setFont(styled.font);
        if (styled.state & QStyle::State_Selected) {
            // KIO chooses Text rather than HighlightedText when Places lacks
            // focus. Both roles must remain readable on the accent backing.
            styled.palette.setColor(QPalette::Text, QColor("#11111b"));
            styled.palette.setColor(QPalette::HighlightedText, QColor("#11111b"));
        }
        m_native->paint(painter, styled, index);
        painter->restore();
    }
    QSize sizeHint(const QStyleOptionViewItem &option, const QModelIndex &index) const override {
        if (!m_native) return QSize();
        QSize size = m_native->sizeHint(option,index);
        // Preserve the existing 24px-icon row height with smaller 16px icons.
        size.rheight() += qMax(0, 24 - qMax(option.decorationSize.height(), option.fontMetrics.height()));
        return size;
    }
    bool helpEvent(QHelpEvent *event, QAbstractItemView *view,
                   const QStyleOptionViewItem &option, const QModelIndex &index) override {
        return m_native && m_native->helpEvent(event,view,option,index);
    }
    bool editorEvent(QEvent *event, QAbstractItemModel *model,
                     const QStyleOptionViewItem &option, const QModelIndex &index) override {
        return m_native && m_native->editorEvent(event,model,option,index);
    }
private:
    QPointer<QAbstractItemDelegate> m_native;
};

// Native alternating rows use fillRect, outside the style API. Keep that palette
// transparent and draw a rounded backing before each file item's native content.
// drawSource preserves text, previews, expansion arrows and selection toggles.
class RowChip : public QGraphicsEffect {
public:
    explicit RowChip(QGraphicsWidget *item) : m_item(item) {}
protected:
    void draw(QPainter *painter) override {
        QRectF bounds = sourceBoundingRect(Qt::LogicalCoordinates);
        if (m_item && m_item->scene() && !m_item->scene()->views().isEmpty()) {
            auto *view = m_item->scene()->views().first();
            const QRectF visible = m_item->mapFromScene(
                view->mapToScene(view->viewport()->rect())).boundingRect();
            // Round the visible row, not the wider offscreen columns.
            bounds = bounds.intersected(visible);
        }
        const bool row = bounds.width() > 140 && bounds.height() <= 64;
        const QRectF *previous = rowPaint;
        int *previousDepth = rowDepth;
        bool *previousFocus = rowFocus;
        rowFocus = row ? &m_focus : nullptr;
        rowPaint = row ? &bounds : nullptr;
        rowDepth = row ? &m_depth : nullptr;
        QPoint offset;
        const QPixmap content = sourcePixmap(Qt::LogicalCoordinates, &offset, NoPad);
        rowDepth = previousDepth;
        rowFocus = previousFocus;
        // Align a nested chip with its parent folder icon: native 20px
        // gutter plus one row-height slot for each expansion level.
        const qreal nestingInset = m_depth > 0 ? 20 + m_depth * bounds.height() : 0;
        const QRectF rect = bounds.adjusted(3 + nestingInset,2,-3,-2);
        if (row) {
            QColor fill("#313244"); fill.setAlpha(90);
            chip(painter, rect, fill);
        }
        painter->save();
        if (row) {
            QPainterPath clip;
            clip.addRoundedRect(rect, qMin<qreal>(6,rect.height()/2), qMin<qreal>(6,rect.height()/2));
            painter->setClipPath(clip, Qt::IntersectClip);
        }
        painter->drawPixmap(offset, content);
        painter->restore();
        if (row && m_focus) chip(painter, rect, Qt::transparent, QColor("#cba6f7"));
        rowPaint = previous;
    }
    void sourceChanged(ChangeFlags flags) override {
        if (flags & SourceInvalidated) m_focus = false;
        QGraphicsEffect::sourceChanged(flags);
    }
private:
    QPointer<QGraphicsWidget> m_item;
    int m_depth = 0;
    bool m_focus = false;
};
class HeaderChip : public QGraphicsEffect {
protected:
    void draw(QPainter *painter) override {
        QColor fill("#313244"); fill.setAlpha(155);
        QColor border("#46485c"); border.setAlpha(150);
        const QRectF bounds = sourceBoundingRect(Qt::LogicalCoordinates);
        chip(painter, bounds.adjusted(3,1,-3,-1), fill, border);
        const QRectF *previous = headerPaint;
        const int previousLast = lastHeaderSection;
        lastHeaderSection = -1;
        headerPaint = &bounds;
        drawSource(painter);
        headerPaint = previous;
        lastHeaderSection = previousLast;
    }
};

// One backing widget paints both arms, so there is no seam between the
// toolbar and Places. It never participates in layout or receives input.
class ShellPanel : public QWidget {
public:
    explicit ShellPanel(QWidget *window) : QWidget(window) {
        setObjectName(QStringLiteral("ricyShellPanel"));
        setAttribute(Qt::WA_TransparentForMouseEvents);
        setAttribute(Qt::WA_NoSystemBackground);
        setFocusPolicy(Qt::NoFocus);
    }
protected:
    void paintEvent(QPaintEvent *) override {
        QWidget *window = parentWidget();
        qreal innerX = width() - 8, innerY = 64;
        bool found = false;
        bool sidebarVisible = false;
        for (auto *child : window->findChildren<QWidget *>()) {
            if (child->inherits("KFilePlacesView") && child->isVisible() && child->window() == window)
                sidebarVisible = true;
            if (!child->inherits("DolphinViewContainer") || !child->isVisible()) continue;
            const QPoint pos = child->mapTo(window, QPoint());
            if (!found || pos.x() < innerX) innerX = pos.x();
            if (!found || pos.y() < innerY) innerY = pos.y();
            found = true;
        }
        const qreal left = 8, top = 8, right = width()-8, bottom = height()-8;
        if (right <= left || bottom <= top) return;
        // File cards have their own 4px top/side margin; the L ends at the outer container
        // edge, leaving that same gutter between the two panels.
        innerX = qBound(left+24, innerX, right);
        innerY = qBound(top+24, innerY, bottom);
        const qreal radius = qMin<qreal>(12, qMin((innerX-left)/2, (innerY-top)/2));
        if (!sidebarVisible) {
            QPainter painter(this);
            painter.setRenderHint(QPainter::Antialiasing);
            painter.setPen(Qt::NoPen);
            painter.setBrush(QColor("#313244"));
            painter.drawRoundedRect(QRectF(left,top,right-left,innerY-top),12,12);
            return;
        }
        QPainterPath path;
        path.moveTo(left+radius, top);
        path.lineTo(right-radius, top);
        path.quadTo(right, top, right, top+radius);
        path.lineTo(right, innerY-radius);
        path.quadTo(right, innerY, right-radius, innerY);
        path.lineTo(innerX+radius, innerY);
        path.quadTo(innerX, innerY, innerX, innerY+radius);
        path.lineTo(innerX, bottom-radius);
        path.quadTo(innerX, bottom, innerX-radius, bottom);
        path.lineTo(left+radius, bottom);
        path.quadTo(left, bottom, left, bottom-radius);
        path.lineTo(left, top+radius);
        path.quadTo(left, top, left+radius, top);
        path.closeSubpath();
        QPainter painter(this);
        painter.setRenderHint(QPainter::Antialiasing);
        painter.setPen(Qt::NoPen);
        painter.setBrush(QColor("#313244"));
        painter.drawPath(path);
    }
};
}

class RicyDolphinUi : public QObject {
public:
    RicyDolphinUi() : QObject(qApp) {
        qApp->installEventFilter(this);
        QTimer::singleShot(0, this, [this] {
            if (QStyle *base = QStyleFactory::create(QStringLiteral("kvantum"))) {
                m_chipStyle = new ChipStyle(base);
                qApp->setStyle(m_chipStyle);
                // Qt's stylesheet wrapper drops PE_IndicatorBranch when Dolphin
                // passes a plain QStyleOption. Graphics items don't use QSS;
                // route them directly to our style to retain folder chevrons.
                for (auto *widget : qApp->allWidgets())
                    if (auto *view = qobject_cast<QGraphicsView *>(widget))
                        if (view->inherits("KItemListContainerViewport") && view->scene())
                            for (auto *item : view->scene()->items())
                                if (auto *graphics = dynamic_cast<QGraphicsWidget *>(item))
                                    graphics->setStyle(m_chipStyle);
                for (auto *widget : qApp->allWidgets())
                    if (widget->inherits("KFilePlacesView")) {
                        QPalette palette = widget->palette();
                        palette.setColor(QPalette::HighlightedText, QColor("#11111b"));
                        palette.setColor(QPalette::Highlight, QColor("#cba6f7"));
                        widget->setPalette(palette);
                    }
            }
        });
    }
    bool eventFilter(QObject *object,QEvent *event) override {
        if (event->type() == QEvent::Resize || event->type() == QEvent::Show)
            if (auto *menu = qobject_cast<QMenu *>(object)) {
                // Match the popup's actual surface to its rounded QSS panel,
                // so native backing cannot remain in the corner cutouts.
                QPainterPath shape;
                shape.addRoundedRect(QRectF(menu->rect()),12,12);
                menu->setMask(QRegion(shape.toFillPolygon().toPolygon()));
            }
        if (event->type() == QEvent::Enter || event->type() == QEvent::Leave)
            if (auto *handle = qobject_cast<QSplitterHandle *>(object)) handle->update();
        if (event->type() == QEvent::MouseButtonPress || event->type() == QEvent::MouseButtonRelease)
            if (auto *handle = qobject_cast<QSplitterHandle *>(object);
                handle && static_cast<QMouseEvent *>(event)->button() == Qt::LeftButton) {
                handle->setProperty("ricyDragging",event->type() == QEvent::MouseButtonPress);
                handle->update();
            }
        // KIO fixes the navigator to the editor's native height when its mode
        // changes. Keep both limits consistent with the padded 36px bar;
        // raising only minimumHeight leaves a smaller native maximumHeight.
        if (event->type() == QEvent::Resize)
            if (auto *widget = qobject_cast<QWidget *>(object);
                widget && widget->inherits("KUrlNavigator") && widget->height() != 36)
                widget->setFixedHeight(36);
        if (event->type() == QEvent::Resize || event->type() == QEvent::LayoutRequest ||
            event->type() == QEvent::Show || event->type() == QEvent::Hide || event->type() == QEvent::Move) {
            auto *widget = qobject_cast<QWidget *>(object);
            if (widget && widget->inherits("DolphinViewContainer")) {
                widget->setAttribute(Qt::WA_StyledBackground);
                const bool rightEdge = widget->mapTo(widget->window(), QPoint(widget->width(),0)).x()
                                       >= widget->window()->width()-12;
                const bool leftEdge = widget->mapTo(widget->window(), QPoint()).x() <= 12;
                if (widget->property("ricyRightEdge").toBool() != rightEdge ||
                    widget->property("ricyLeftEdge").toBool() != leftEdge) {
                    widget->setProperty("ricyRightEdge",rightEdge);
                    widget->setProperty("ricyLeftEdge",leftEdge);
                    widget->style()->unpolish(widget);
                    widget->style()->polish(widget);
                    widget->update();
                }
                // QSS only paints this QWidget's margin; reserve the actual
                // 4px top/side gutter plus 8px inner padding in the native layout.
                // Keep the outer right/bottom window margins at their original 8px.
                if (widget->layout()) widget->layout()->setContentsMargins(leftEdge?16:12,12,rightEdge?16:12,16);
            }
            if (auto *dock = qobject_cast<QDockWidget *>(widget);
                dock && dock->widget() && dock->widget()->inherits("KFilePlacesView"))
                dock->setContentsMargins(0,0,0,12);
            auto *window = widget ? widget->window() : nullptr;
            if (window && window->inherits("DolphinMainWindow") &&
                (widget == window || widget->inherits("KItemListContainer") ||
                 widget->inherits("DolphinViewContainer") ||
                 widget->inherits("QDockWidget"))) {
                auto *panel = window->findChild<QWidget *>(QStringLiteral("ricyShellPanel"), Qt::FindDirectChildrenOnly);
                if (!panel) panel = new ShellPanel(window);
                panel->setGeometry(window->rect());
                panel->lower();
                panel->show();
                panel->update();
            }
        }
        // QSS positions Dolphin's native tab close buttons at the outer edge.
        // Keep the native buttons/signals, but align their actual hit rectangles
        // inside the pill after Qt has finished laying out the tab bar.
        if (event->type() == QEvent::Paint) {
            if (auto *handle = qobject_cast<QSplitterHandle *>(object)) {
                bool filePanels = false;
                for (auto *child : handle->splitter()->findChildren<QWidget *>())
                    if (child->inherits("DolphinViewContainer")) { filePanels = true; break; }
                if (filePanels) {
                    QPainter painter(handle);
                    painter.setRenderHint(QPainter::Antialiasing);
                    painter.setPen(Qt::NoPen);
                    QColor color("#242435");
                    if (handle->property("ricyDragging").toBool()) color = QColor("#cba6f7");
                    else if (handle->underMouse()) { color = QColor("#a6adc8"); color.setAlpha(128); }
                    painter.setBrush(color);
                    const bool horizontal = handle->orientation() == Qt::Horizontal;
                    const QRectF line = horizontal
                        ? QRectF((handle->width()-2)/2.0,12,2,qMax(0,handle->height()-24))
                        : QRectF(12,(handle->height()-2)/2.0,qMax(0,handle->width()-24),2);
                    painter.drawRoundedRect(line,1,1);
                    return true;
                }
            }
            if (auto *tabs = qobject_cast<QTabBar *>(object)) {
                QRect available = tabs->rect();
                for (auto *arrow : tabs->findChildren<QToolButton *>(QString(), Qt::FindDirectChildrenOnly)) {
                    if (!arrow->isVisible() || (arrow->objectName() != QStringLiteral("ScrollLeftButton") &&
                                               arrow->objectName() != QStringLiteral("ScrollRightButton"))) continue;
                    if (tabs->layoutDirection() == Qt::RightToLeft)
                        available.setLeft(qMax(available.left(), arrow->geometry().right() + 9));
                    else
                        available.setRight(qMin(available.right(), arrow->geometry().left() - 9));
                    arrow->raise();
                }
                for (int index = 0; index < tabs->count(); ++index) {
                    const QRect rect = tabs->tabRect(index);
                    for (auto side : {QTabBar::LeftSide, QTabBar::RightSide}) {
                        auto *button = tabs->tabButton(index, side);
                        if (!button) continue;
                        const bool left = (side == QTabBar::LeftSide) !=
                                          (tabs->layoutDirection() == Qt::RightToLeft);
                        const int x = left ? rect.left() + 12
                                           : rect.right() - 11 - button->width();
                        const QPoint position(x, rect.center().y() - button->height()/2);
                        if (button->pos() != position) button->move(position);
                        // A clipped tab must not leave an active close button
                        // over the scroll controls or outside the visible strip.
                        if (available.contains(button->geometry())) button->clearMask();
                        else button->setMask(QRegion(QRect(-1,-1,1,1)));
                    }
                }
            }
        }
        if(event->type() == QEvent::Polish) {
            auto *widget = qobject_cast<QWidget *>(object);
            // Let QSS rounded popup corners expose the desktop, not a square
            // native backing. Preserve Qt popup flags and all menu actions.
            if (auto *menu = qobject_cast<QMenu *>(widget)) {
                menu->setAttribute(Qt::WA_TranslucentBackground);
                menu->setAttribute(Qt::WA_OpaquePaintEvent, false);
                menu->setAutoFillBackground(false);
                QPalette palette = menu->palette();
                palette.setColor(QPalette::Window, Qt::transparent);
                menu->setPalette(palette);
            }
            if (auto *tabs = qobject_cast<QTabBar *>(widget)) tabs->setDrawBase(false);
            if (widget && widget->inherits("KUrlNavigator")) {
                widget->setAttribute(Qt::WA_StyledBackground);
                widget->setFixedHeight(36);
                if (widget->layout()) widget->layout()->setContentsMargins(8,0,8,0);
            }
            // Newly created segments inherit the navigator's minimum height.
            // Give every direct button the same 28px content slot inside its
            // 36px parent, rather than mixing 28px and clipped 36px segments.
            if (widget && widget->parentWidget() && widget->parentWidget()->inherits("KUrlNavigator") &&
                qobject_cast<QAbstractButton *>(widget)) widget->setFixedHeight(28);
            // The native path dropdown's size hint uses half its natural font
            // height. Reserve the existing 24px control slot so the shared
            // rounded hover backing fits inside its actual paint/hit bounds.
            if (widget && QByteArray(widget->metaObject()->className()).contains("KUrlNavigatorDropDownButton"))
                widget->setFixedWidth(24);
            if (widget && widget->parentWidget() && widget->parentWidget()->inherits("KUrlNavigator") &&
                qobject_cast<QComboBox *>(widget)) widget->setFixedHeight(36);
            if (widget && widget->inherits("KFilePlacesView"))
                if (auto *places = qobject_cast<QListView *>(widget)) {
                    places->setSpacing(3);
                    places->setIconSize(QSize(16,16));
                    QFont font = places->font();
                    font.setWeight(QFont::DemiBold);
                    places->setFont(font);
                    if (!places->itemDelegateForColumn(0))
                        places->setItemDelegateForColumn(0, new PlacesResultPaint(places->itemDelegate(),places));
                    QPalette palette = places->palette();
                    for (auto group : {QPalette::Active, QPalette::Inactive, QPalette::Disabled}) {
                        palette.setColor(group, QPalette::HighlightedText, QColor("#11111b"));
                        palette.setColor(group, QPalette::Highlight, QColor("#cba6f7"));
                    }
                    places->setPalette(palette);
                    places->viewport()->setPalette(palette);
                }
            if(widget && widget->inherits("DolphinMainWindow") && !widget->testAttribute(Qt::WA_WState_Created))
                widget->setAttribute(Qt::WA_TranslucentBackground,true);
            auto *item = qobject_cast<QGraphicsWidget *>(object);
            if(item && m_chipStyle) item->setStyle(m_chipStyle);
            if(item && item->inherits("KItemListWidget") && !item->graphicsEffect())
                item->setGraphicsEffect(new RowChip(item));
            if(item && item->inherits("KItemListHeaderWidget") && !item->graphicsEffect()) {
                item->setFont(QFont(QStringLiteral("Noto Sans"), 10));
                item->setGraphicsEffect(new HeaderChip);
            }
        }
        return false;
    }
private:
    QPointer<QStyle> m_chipStyle;
};
class RicyDolphinUiPlugin : public QGenericPlugin {
    Q_OBJECT
    Q_PLUGIN_METADATA(IID "org.qt-project.Qt.QGenericPluginFactoryInterface" FILE "ui.json")
public:
    QObject *create(const QString &name,const QString &) override {
        if(name == QStringLiteral("ricydolphinui") && QCoreApplication::applicationName() == QStringLiteral("dolphin"))
            return new RicyDolphinUi;
        return nullptr;
    }
};
#include "ui.moc"
