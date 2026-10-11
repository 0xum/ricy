#!/usr/bin/python
import os
from pathlib import Path
import sys
from PyQt6.QtCore import QThread, pyqtSignal, Qt, QTimer
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
                            QPlainTextEdit, QProgressBar, QFileDialog, QMessageBox)
import backend


class Worker(QThread):
    line = pyqtSignal(str)
    result = pyqtSignal(object)

    def __init__(self, action, filename):
        super().__init__()
        self.action, self.filename = action, filename

    def run(self):
        try:
            value = self.action(self.filename, self.line.emit)
            self.result.emit((True, value))
        except Exception as exc:
            self.result.emit((False, str(exc)))


class Installer(QWidget):
    def __init__(self, filename=None):
        super().__init__()
        self.filename, self.package, self.busy = filename, None, False
        self.setWindowTitle('Install Package on CachyOS')
        self.resize(760, 520)
        layout = QVBoxLayout(self)
        self.label = QLabel()
        self.label.setTextFormat(Qt.TextFormat.PlainText)
        self.label.setWordWrap(True)
        layout.addWidget(self.label)
        self.note = QLabel('The package will be converted to CachyOS format. '
                           'Installation remains managed by pacman.')
        self.note.setWordWrap(True)
        layout.addWidget(self.note)
        self.info = QPlainTextEdit()
        self.info.setReadOnly(True)
        layout.addWidget(self.info)
        self.progress = QProgressBar()
        self.progress.hide()
        layout.addWidget(self.progress)
        self.button = QPushButton('Prepare Package' if filename else 'Select .deb or .rpm')
        self.button.clicked.connect(self.clicked)
        layout.addWidget(self.button)
        self.status = QLabel('')
        self.status.setTextFormat(Qt.TextFormat.PlainText)
        self.status.setWordWrap(True)
        layout.addWidget(self.status)
        self.label.setText(Path(filename).name if filename else 'Choose a local package to install.')
        self.logs = []
        if filename:
            QTimer.singleShot(0, self.clicked)

    def clicked(self):
        if self.busy:
            return
        if not self.filename:
            filename, _ = QFileDialog.getOpenFileName(self, 'Select Package',
                str(Path.home() / 'Downloads'), 'Packages (*.deb *.rpm)')
            if not filename:
                return
            self.filename = filename
            self.label.setText(Path(filename).name)
        self.installing = bool(self.package)
        self.busy = True
        self.button.setEnabled(False)
        self.progress.setRange(0, 0)
        self.progress.show()
        self.status.setText('Installing… Authorize in the system password dialog.' if self.installing
                            else 'Converting and checking dependencies… This may take a few minutes.')
        self.worker = Worker(backend.install if self.installing else backend.prepare,
                             self.package or self.filename)
        self.worker.line.connect(self.log)
        self.worker.result.connect(self.completed)
        self.worker.start()

    def log(self, line):
        self.logs.append(line)
        self.info.appendPlainText(line)

    def completed(self, result):
        self.worker.wait()
        self.busy = False
        self.progress.hide()
        ok, value = result
        if not ok:
            self.status.setText(value)
            self.button.setText('Try Again')
            self.button.setEnabled(True)
        elif self.installing:
            self.status.setText('Package installed successfully. If it provides an application, find it in the menu.')
            self.button.setText('Installed')
        else:
            self.package, info = value
            self.info.setPlainText(info)
            self.status.setText('Package prepared. Click Install to confirm the installation.')
            self.button.setText('Install')
            self.button.setEnabled(True)
        if self.logs:
            backend.CACHE.mkdir(parents=True, exist_ok=True)
            (backend.CACHE / 'last-conversion.log').write_text('\n'.join(self.logs))

    def closeEvent(self, event):
        if self.busy:
            QMessageBox.information(self, 'Operation in progress',
                                    'Wait for the operation to finish before closing this window.')
            event.ignore()
        else:
            event.accept()


if __name__ == '__main__':
    if os.geteuid() == 0:
        sys.exit('Open the installer as a normal user.')
    app = QApplication(sys.argv)
    app.setDesktopFileName('cachyos-local-package-installer')
    window = Installer(sys.argv[1] if len(sys.argv) > 1 else None)
    window.show()
    sys.exit(app.exec())
