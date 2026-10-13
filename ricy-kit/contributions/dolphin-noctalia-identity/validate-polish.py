#!/usr/bin/env python3
"""Offline Qt state/interaction checks; never install or change desktop settings."""
import argparse
import json
import os
from pathlib import Path
import sys

os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')
try:
    from PyQt6.QtCore import QPoint, Qt, qInstallMessageHandler
    from PyQt6.QtGui import QColor
    from PyQt6.QtTest import QTest
    from PyQt6.QtWidgets import QAbstractButton, QApplication, QCheckBox, QComboBox, QDialog, QDockWidget, QLineEdit, QListWidget, QMainWindow, QMenu, QPushButton, QSlider, QSpinBox, QStyleFactory, QTabWidget, QToolBar, QToolButton, QVBoxLayout, QWidget
except ImportError:
    print('NOT RUN Qt state checks: PyQt6 unavailable')
    sys.exit(2)

here = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--stylesheet', type=Path, default=here / 'dolphin.qss')
arguments = parser.parse_args()
root = here.parents[2]
tokens = json.loads((root / 'themes/tokens/tokens.json').read_text())
colors = tokens['colors']
dolphin = tokens['application_adaptations']['dolphin']
messages = []
qInstallMessageHandler(lambda kind, context, message: messages.append(message))
app = QApplication(['ricy-polish-validation'])
app.setStyle(QStyleFactory.create('kvantum') or QStyleFactory.create('Fusion'))
app.setStyleSheet(arguments.stylesheet.read_text())
window = QMainWindow()
bar = QToolBar(window)
window.addToolBar(bar)
button = QToolButton()
button.setCheckable(True)
button.setText("Split")
bar.addWidget(button)
other = QToolButton()
bar.addWidget(other)
editor = QLineEdit()
window.setCentralWidget(editor)
window.resize(640, 240)
window.show()
QTest.qWait(60)


def pixel(widget, x, y):
    capture = widget.grab().toImage()
    ratio = capture.devicePixelRatio()
    return capture.pixelColor(round(x * ratio), round(y * ratio))


def has_color(widget, color):
    capture = widget.grab().toImage()
    expected = QColor(color)
    return any(capture.pixelColor(x, y) == expected
               for y in range(capture.height()) for x in range(capture.width()))


# Exercise the precedence bug: hovering a checked native toolbar action must
# retain its action fill and foreground rather than becoming an unselected row.
button.setChecked(True)
QTest.mouseMove(button, button.rect().center())
QTest.qWait(30)
assert pixel(button, 4, button.height() // 2) == QColor(colors['hover_selection'])
assert has_color(button, colors['on_hover_selection'])
minimum = dolphin['toolbar']['button_minimum_size']
assert button.width() >= minimum and button.height() >= minimum
size = button.size()
button.setChecked(False)
button.setFocus()
QTest.qWait(30)
assert button.hasFocus()
assert pixel(button, 0, button.height() // 2) == QColor(colors['accent'])
assert button.size() == size  # Focus adds no layout shift or smaller hit area.
clicked = []
button.clicked.connect(clicked.append)
QTest.mousePress(button, Qt.MouseButton.LeftButton)
QTest.qWait(20)
assert pixel(button, 4, button.height() // 2) == QColor(colors['hover_selection'])
QTest.mouseRelease(button, Qt.MouseButton.LeftButton)
assert clicked == [True]
button.setEnabled(False)
QTest.qWait(30)
assert has_color(button, colors['secondary_text'])
QTest.mouseClick(button, Qt.MouseButton.LeftButton)
assert clicked == [True]
editor.setText('Native path text')
editor.setFocus()
editor.selectAll()
QTest.keyClicks(editor, 'Replacement')
assert editor.text() == 'Replacement'

# Retain native tab keyboard navigation/close signals and menu invocation;
# these checks do not certify helper overflow geometry or compositor masks.
tabs = QTabWidget()
tabs.setTabsClosable(True)
for title in ('Documents', 'Music', 'Downloads'):
    tabs.addTab(QWidget(), title)
tabs.resize(600, 180)
tabs.show()
QTest.qWait(30)
tabbar = tabs.tabBar()
tabbar.setFocus()
QTest.keyClick(tabbar, Qt.Key.Key_Right)
assert tabs.currentIndex() == 1
closed = []
tabs.tabCloseRequested.connect(closed.append)
close = tabbar.tabButton(1, tabbar.ButtonPosition.RightSide)
assert close is not None
QTest.mouseClick(close, Qt.MouseButton.LeftButton)
assert closed == [1]
menu = QMenu()
action = menu.addAction('Inspect')
unavailable = menu.addAction('Unavailable')
unavailable.setEnabled(False)
submenu = menu.addMenu('Native submenu')
submenu.addAction('Native child')
invoked = []
action.triggered.connect(lambda: invoked.append(True))
menu.popup(QPoint(20, 20))
QTest.qWait(30)
menu.setActiveAction(action)
rect = menu.actionGeometry(action)
assert pixel(menu, rect.center().x(), rect.top() + 3) == QColor(colors['accent'])
QTest.keyClick(menu, Qt.Key.Key_Return)
assert invoked == [True] and not unavailable.isEnabled()
assert len(submenu.actions()) == 1

# Dialog rules must preserve native settings controls and keyboard access.
dialog = QDialog()
layout = QVBoxLayout(dialog)
apply_button = QPushButton('Apply')
choice = QComboBox()
choice.addItems(['First', 'Second'])
number = QSpinBox()
toggle = QCheckBox('Enabled')
items = QListWidget()
items.addItems(['First', 'Second'])
zoom = QSlider(Qt.Orientation.Horizontal)
zoom.setRange(0, 100)
zoom.setValue(50)
for control in (apply_button, choice, number, toggle, items, zoom):
    layout.addWidget(control)
dialog.resize(400, 480)
dialog.show()
QTest.qWait(50)
dialog_clicked = []
apply_button.clicked.connect(lambda: dialog_clicked.append(True))
apply_button.setFocus()
assert pixel(apply_button, 0, apply_button.height() // 2) == QColor(colors['accent'])
button_size = apply_button.size()
QTest.mouseClick(apply_button, Qt.MouseButton.LeftButton)
assert dialog_clicked == [True]
apply_button.setEnabled(False)
QTest.mouseClick(apply_button, Qt.MouseButton.LeftButton)
assert dialog_clicked == [True] and apply_button.size() == button_size
assert has_color(apply_button, colors['secondary_text'])
choice.setFocus()
QTest.keyClick(choice, Qt.Key.Key_Down)
assert choice.currentIndex() == 1
number.setFocus()
QTest.keyClick(number, Qt.Key.Key_Up)
assert number.value() == 1
toggle.setFocus()
QTest.keyClick(toggle, Qt.Key.Key_Space)
assert toggle.isChecked()
items.setCurrentRow(0)
items.setFocus()
QTest.keyClick(items, Qt.Key.Key_Down)
assert items.currentRow() == 1
assert has_color(items.viewport(), colors['accent'])
zoom.setFocus()
QTest.keyClick(zoom, Qt.Key.Key_Right)
assert zoom.value() == 51 and has_color(zoom, colors['accent'])
QTest.keyClick(dialog, Qt.Key.Key_Escape)
assert not dialog.isVisible()
# Dock styling must retain the actual Qt close action and native reopen route.
dock = QDockWidget('Information', window)
dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetClosable | QDockWidget.DockWidgetFeature.DockWidgetMovable)
dock.setWidget(QWidget())
window.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)
window.resize(800, 480)
window.show()
QTest.qWait(50)
dock_close = dock.findChild(QAbstractButton, 'qt_dockwidget_closebutton')
assert dock_close is not None and dock_close.isVisible()
# The 24px allocation belongs to the helper and is checked by the native fixture.
assert dock_close.width() > 0 and dock_close.height() > 0
assert dock.rect().contains(dock_close.geometry())
QTest.mouseMove(window, QPoint(8, window.height() - 8))
QTest.qWait(30)
QTest.mouseMove(dock_close, dock_close.rect().center())
QTest.qWait(30)
QTest.mousePress(dock_close, Qt.MouseButton.LeftButton)
QTest.qWait(20)
assert dock_close.isDown()
QTest.mouseRelease(dock_close, Qt.MouseButton.LeftButton)
QTest.qWait(20)
assert not dock.isVisible() and not dock.toggleViewAction().isChecked()
dock.toggleViewAction().trigger()
QTest.qWait(20)
assert dock.isVisible() and dock.toggleViewAction().isChecked()
# Dolphin supplies a zero-height native title widget while panels are locked.
locked_title = QWidget()
locked_title.setFixedHeight(0)
dock.setTitleBarWidget(locked_title)
QTest.qWait(20)
assert not dock_close.isVisible()
dock.setTitleBarWidget(None)
QTest.qWait(20)
assert dock_close.isVisible()
errors = [message for message in messages if 'stylesheet' in message.lower() or 'unknown property' in message.lower()]
assert not errors, errors
print(f'PASS QSS parsing, toolbar hover/checked/pressed/disabled/focus and fixed hit areas; native editor/tab/menu interactions; scale={window.devicePixelRatioF():g}')
print('PASS dialog button focus/disabled and native combo/spin/check/list/zoom keyboard access; Escape dismisses without applying')
print('PASS native dock close/reopen, pressed input, and locked/unlocked title visibility')
print('NOT RUN compositor, helper masks, real file operations and live Recovery')
