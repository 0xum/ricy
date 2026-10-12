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
    from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow, QMenu, QStyleFactory, QTabWidget, QToolBar, QToolButton, QWidget
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
errors = [message for message in messages if 'stylesheet' in message.lower() or 'unknown property' in message.lower()]
assert not errors, errors
print(f'PASS QSS parsing, toolbar hover/checked/pressed/disabled/focus and fixed hit areas; native editor/tab/menu interactions; scale={window.devicePixelRatioF():g}')
print('NOT RUN compositor, helper masks, real file operations and live Recovery')
