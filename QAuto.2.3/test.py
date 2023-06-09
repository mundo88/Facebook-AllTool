import os
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets, uic


class Worker(QtCore.QObject):
    textChanged = QtCore.pyqtSignal(str)
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()

    @QtCore.pyqtSlot()
    def run_task(self):
        self.started.emit()
        self.textChanged.emit("Func 1")
        time.sleep(3)  # in real app do something here
        self.textChanged.emit("Func 2")
        time.sleep(3)  # in real app do something else here
        self.textChanged.emit("Func 3")
        self.finished.emit()


class TestWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        relpath = "ui/test.ui"
        current_dir = os.path.dirname(os.path.realpath(__file__))
        uifile = os.path.join(current_dir, relpath)
        uic.loadUi(uifile, self)

        thread = QtCore.QThread(self)
        thread.start()

        self.m_worker = Worker()
        self.m_worker.moveToThread(thread)
        self.m_worker.started.connect(self.onStarted)
        self.m_worker.finished.connect(self.onFinished)
        self.m_worker.textChanged.connect(self.update_label)

        self.pushButton.clicked.connect(self.m_worker.run_task)
        self.progressBar.setValue(0)

    @QtCore.pyqtSlot()
    def onStarted(self):
        self.progressBar.setMaximum(0)
        self.pushButton.setEnabled(False)

    @QtCore.pyqtSlot()
    def onFinished(self):
        self.progressBar.setMaximum(1)
        self.progressBar.setValue(1)
        self.pushButton.setEnabled(True)

    @QtCore.pyqtSlot(str)
    def update_label(self, text):
        self.label.setText(text)