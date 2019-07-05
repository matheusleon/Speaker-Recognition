# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecordAudioWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RecordAudioWindow(object):
    def setupUi(self, RecordAudioWindow):
        RecordAudioWindow.setObjectName("RecordAudioWindow")
        RecordAudioWindow.resize(616, 359)
        self.verticalLayout = QtWidgets.QVBoxLayout(RecordAudioWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(RecordAudioWindow)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.widget_4)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_4.addWidget(self.lcdNumber)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(RecordAudioWindow)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 45))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.directoryButton = QtWidgets.QPushButton(self.widget_3)
        self.directoryButton.setObjectName("directoryButton")
        self.horizontalLayout_3.addWidget(self.directoryButton)
        self.directoryText = QtWidgets.QTextBrowser(self.widget_3)
        self.directoryText.setLineWidth(0)
        self.directoryText.setObjectName("directoryText")
        self.horizontalLayout_3.addWidget(self.directoryText)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(RecordAudioWindow)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 45))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fileName = QtWidgets.QLabel(self.widget_2)
        self.fileName.setObjectName("fileName")
        self.horizontalLayout_2.addWidget(self.fileName)
        self.fileText = QtWidgets.QTextEdit(self.widget_2)
        self.fileText.setMaximumSize(QtCore.QSize(16777215, 65))
        self.fileText.setObjectName("fileText")
        self.horizontalLayout_2.addWidget(self.fileText)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(RecordAudioWindow)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.secondsBox = QtWidgets.QSpinBox(self.widget_5)
        self.secondsBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.secondsBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.secondsBox.setMinimum(1)
        self.secondsBox.setMaximum(60)
        self.secondsBox.setObjectName("secondsBox")
        self.horizontalLayout_5.addWidget(self.secondsBox)
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.widget_5)
        self.startButton = QtWidgets.QPushButton(self.widget)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout.addWidget(self.startButton)
        self.verticalLayout.addWidget(self.widget)
        self.closeButton = QtWidgets.QPushButton(RecordAudioWindow)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)

        self.retranslateUi(RecordAudioWindow)
        QtCore.QMetaObject.connectSlotsByName(RecordAudioWindow)

    def retranslateUi(self, RecordAudioWindow):
        _translate = QtCore.QCoreApplication.translate
        RecordAudioWindow.setWindowTitle(_translate("RecordAudioWindow", "Record Audio"))
        self.directoryButton.setText(_translate("RecordAudioWindow", "Choose Directory"))
        self.fileName.setText(_translate("RecordAudioWindow", "File Name:"))
        self.fileText.setHtml(_translate("RecordAudioWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">output.wav</p></body></html>"))
        self.label_2.setText(_translate("RecordAudioWindow", "seconds"))
        self.startButton.setText(_translate("RecordAudioWindow", "Record"))
        self.closeButton.setText(_translate("RecordAudioWindow", "Close"))
