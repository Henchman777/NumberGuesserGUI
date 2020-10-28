# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(551, 439)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.maxNumSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.maxNumSpinBox.setGeometry(QtCore.QRect(390, 290, 42, 22))
        self.maxNumSpinBox.setMinimum(-100000)
        self.maxNumSpinBox.setMaximum(100000)
        self.maxNumSpinBox.setProperty("value", 20)
        self.maxNumSpinBox.setObjectName("maxNumSpinBox")
        self.maxNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxNumLabel.setGeometry(QtCore.QRect(320, 290, 71, 20))
        self.maxNumLabel.setObjectName("maxNumLabel")
        self.titileLabel = QtWidgets.QLabel(self.centralwidget)
        self.titileLabel.setEnabled(True)
        self.titileLabel.setGeometry(QtCore.QRect(40, 20, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.titileLabel.setFont(font)
        self.titileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titileLabel.setObjectName("titileLabel")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(320, 340, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.quitButton.setFont(font)
        self.quitButton.setObjectName("quitButton")
        self.informationLabel = QtWidgets.QLabel(self.centralwidget)
        self.informationLabel.setGeometry(QtCore.QRect(90, 80, 391, 101))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.informationLabel.setFont(font)
        self.informationLabel.setWordWrap(True)
        self.informationLabel.setObjectName("informationLabel")
        self.minNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.minNumLabel.setGeometry(QtCore.QRect(110, 290, 71, 20))
        self.minNumLabel.setObjectName("minNumLabel")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(100, 340, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.minNumSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.minNumSpinBox.setGeometry(QtCore.QRect(180, 290, 42, 22))
        self.minNumSpinBox.setMinimum(-100000)
        self.minNumSpinBox.setMaximum(100000)
        self.minNumSpinBox.setObjectName("minNumSpinBox")
        self.highScoreMain = QtWidgets.QLabel(self.centralwidget)
        self.highScoreMain.setGeometry(QtCore.QRect(190, 240, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.highScoreMain.setFont(font)
        self.highScoreMain.setObjectName("highScoreMain")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.maxNumLabel.setText(_translate("MainWindow", "High Number"))
        self.titileLabel.setText(_translate("MainWindow", "Random Number Guesser"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
        self.informationLabel.setText(_translate("MainWindow", "To play, choose to numbers between -100,000 and 100,000 and try to guess the number, chosen by the computer."))
        self.minNumLabel.setText(_translate("MainWindow", "Low Number"))
        self.startButton.setText(_translate("MainWindow", "Play"))
        self.highScoreMain.setText(_translate("MainWindow", "TextLabel"))

