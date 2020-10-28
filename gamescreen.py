# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gamescreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GameScreen(object):
    def setupUi(self, GameScreen):
        GameScreen.setObjectName("GameScreen")
        GameScreen.resize(393, 260)
        self.highScoreGame = QtWidgets.QLabel(GameScreen)
        self.highScoreGame.setGeometry(QtCore.QRect(30, 20, 141, 16))
        self.highScoreGame.setObjectName("highScoreGame")
        self.currentScore = QtWidgets.QLabel(GameScreen)
        self.currentScore.setGeometry(QtCore.QRect(30, 50, 141, 16))
        self.currentScore.setObjectName("currentScore")
        self.chooseANumberLabel = QtWidgets.QLabel(GameScreen)
        self.chooseANumberLabel.setGeometry(QtCore.QRect(30, 130, 301, 41))
        self.chooseANumberLabel.setWordWrap(True)
        self.chooseANumberLabel.setObjectName("chooseANumberLabel")
        self.userInputSpinBox = QtWidgets.QSpinBox(GameScreen)
        self.userInputSpinBox.setGeometry(QtCore.QRect(100, 190, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userInputSpinBox.setFont(font)
        self.userInputSpinBox.setMinimum(-1000000)
        self.userInputSpinBox.setMaximum(1000000)
        self.userInputSpinBox.setObjectName("userInputSpinBox")
        self.submitButton = QtWidgets.QPushButton(GameScreen)
        self.submitButton.setGeometry(QtCore.QRect(200, 190, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")

        self.retranslateUi(GameScreen)
        QtCore.QMetaObject.connectSlotsByName(GameScreen)

    def retranslateUi(self, GameScreen):
        _translate = QtCore.QCoreApplication.translate
        GameScreen.setWindowTitle(_translate("GameScreen", "Form"))
        self.highScoreGame.setText(_translate("GameScreen", "TextLabel"))
        self.currentScore.setText(_translate("GameScreen", "TextLabel"))
        self.chooseANumberLabel.setText(_translate("GameScreen", "TextLabel"))
        self.submitButton.setText(_translate("GameScreen", "Submit Guess"))

