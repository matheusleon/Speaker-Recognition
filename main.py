import matplotlib
matplotlib.use('Agg')

from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QFileDialog, QLayout, QLabel
import os
import sys
import time

import ml
import MFCC
import audio

import _thread
import threading
import MainWindow
import RecordAudioWindow

import sys
import time

import numpy as np

from scipy.io import loadmat
from scipy.io.wavfile import read, write

from matplotlib.figure import Figure
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar

class WhoAmIWindowClass(QtWidgets.QMainWindow):
  def __init__(self, mlres):
    super().__init__()
    self._main = QtWidgets.QWidget()
    self.setCentralWidget(self._main)
    layout = QtWidgets.QVBoxLayout(self._main)

    nomes = ['Beza', 'Leon', 'Clodes', 'Mendes', 'Jose\'']
    labelText = QtWidgets.QLabel(self)
    labelText.setText('Provalvelmente vc eh: ' + nomes[mlres[0]])
    layout.addWidget(labelText)
    photo = QLabel()
    
    img = QtGui.QPixmap()

    if (nomes[mlres[0]] == 'Beza'):
      img = QtGui.QPixmap('beza.jpeg')
    img = img.scaled(500, 500, QtCore.Qt.KeepAspectRatio)

    photo.setPixmap(img)
    layout.addWidget(photo)
"""
    static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
    layout.addWidget(static_canvas)
    self.addToolBar(NavigationToolbar(static_canvas, self))

    dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
    layout.addWidget(dynamic_canvas)
    self.addToolBar(QtCore.Qt.BottomToolBarArea,
                    NavigationToolbar(dynamic_canvas, self))

    self._static_ax = static_canvas.figure.subplots()
    t = np.linspace(0, 10, 501)
    self._static_ax.plot(t, np.tan(t), ".")

    self._dynamic_ax = dynamic_canvas.figure.subplots()
    self._timer = dynamic_canvas.new_timer(
        100, [(self._update_canvas, (), {})])
    self._timer.start()

  def _update_canvas(self):
    self._dynamic_ax.clear()
    t = np.linspace(0, 10, 101)
    # Shift the sinusoid as a function of time.
    self._dynamic_ax.plot(t, np.sin(t + time.time()))
    self._dynamic_ax.figure.canvas.draw()
"""
class RecordAudioWindowClass(QtWidgets.QDialog, RecordAudioWindow.Ui_RecordAudioWindow):
  def __init__(self, parent = None):
    super(RecordAudioWindowClass, self).__init__(parent)
    self.setupUi(self)
    self.directoryPath = ''
    self.lcdNumber.display('00:00')
    self.record = False
    self.file = ''
    self.run()

  def changeLcdValue(self, value):
    m, s = divmod(value, 60)
    self.lcdNumber.display('{:02d}:{:02d}'.format(m, s))
    self.lcdNumber.repaint()

  def recordAudio(self, duration, file):
    audio.record(duration, file)
  
  def updateWaveform(self):
    img = QtGui.QPixmap('tmp_waveform.png')
    img = img.scaled(self.label.size())
    self.label.setContentsMargins(0, 0, 0, 0)
    self.label.setPixmap(img)

  def lcdCountdown(self, timer):
    while (timer >= 0):
      print(timer)
      self.changeLcdValue(timer)
      time.sleep(1)
      timer -= 1

  def getDirectoryPath(self):
    file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
    self.directoryPath = file
    self.directoryText.setText(file)

  def closeWindow(self):
    self.close()

  def run(self):
    self.directoryText.setText('/')
    self.startButton.clicked.connect(self.startRecord)
    self.directoryButton.clicked.connect(self.getDirectoryPath)
    self.closeButton.clicked.connect(self.closeWindow)

  def showLcdNumber(self):
    self.lcdNumber.show(self)

  def audioImage(self):
    while self.record:
      audio.plot_audio('tmp_waveform.png')
      self.updateWaveform()

  def startRecord(self):
    file = self.directoryPath
    if file != "":
      file += '/'
    file += self.fileText.toPlainText()
    print(file)
    duration = int(self.secondsBox.value())
    t1 = Thread(target = self.lcdCountdown, args = [duration])
    t1.start()
    t2 = Thread(target = self.recordAudio, args = [duration, file])
    t2.start()
    self.record = True
    t3 = Thread(target = self.audioImage, args = [])
    t3.start()
    t1.join()
    t2.join()
    self.record = False
    t3.join()
    img = QtGui.QPixmap()
    img = img.scaled(self.label.size())
    self.label.setContentsMargins(0, 0, 0, 0)
    self.label.setPixmap(img)

class MainWindowClass(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
  def __init__(self, parent = None):
    super(MainWindowClass, self).__init__(parent)
    self.setupUi(self)
    self.run()

  def openRecordAudioWindow(self):
    self.recordAudioWindow = RecordAudioWindowClass()
    self.recordAudioWindow.show()

  def selectFile(self):
    self.file = QFileDialog.getOpenFileName(self, "Select file to open")
    self.fileNameText.setText(self.file[0])
    print('here')
    if (self.file != ''):
      self.whoAmIButton.setEnabled(True)
      print(self.file)
    else:
      print('Empty file!')

  def getPerson(self):
    if self.file[0] == '':
      print('empty file!')
      return
    sample_rate, signal = read(self.file[0])
    theta1 = loadmat('ml.mat')['theta1']
    theta2 = loadmat('ml.mat')['theta2']
    mfcc = MFCC.main(signal, sample_rate)
    mlres = ml.predictWAV(theta1, theta2, mfcc)
    self.whoAmIWindow = WhoAmIWindowClass(mlres)
    self.whoAmIWindow.setWindowTitle('Result')
    self.whoAmIWindow.show()

  def run(self):
    self.whoAmIButton.setEnabled(False)
    self.recordAudioButton.clicked.connect(self.openRecordAudioWindow)
    self.openAudioButton.clicked.connect(self.selectFile)
    self.whoAmIButton.clicked.connect(self.getPerson)

def main():
  app = QApplication(sys.argv)

  mainWindow = MainWindowClass()
  mainWindow.show()

  return app.exec_()

if __name__ == '__main__':
  sys.exit(main())
