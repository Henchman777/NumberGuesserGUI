# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youwin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_YouWinScreen(object):
    def setupUi(self, YouWinScreen):
        YouWinScreen.setObjectName("YouWinScreen")
        YouWinScreen.resize(400, 300)
        self.youGuessedNumberLabel = QtWidgets.QLabel(YouWinScreen)
        self.youGuessedNumberLabel.setGeometry(QtCore.QRect(150, 50, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.youGuessedNumberLabel.setFont(font)
        self.youGuessedNumberLabel.setObjectName("youGuessedNumberLabel")
        self.scoreYouWinLabel = QtWidgets.QLabel(YouWinScreen)
        self.scoreYouWinLabel.setGeometry(QtCore.QRect(110, 140, 180, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scoreYouWinLabel.setFont(font)
        self.scoreYouWinLabel.setObjectName("scoreYouWinLabel")
        self.highScoreWinLabel = QtWidgets.QLabel(YouWinScreen)
        self.highScoreWinLabel.setGeometry(QtCore.QRect(110, 180, 180, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.highScoreWinLabel.setFont(font)
        self.highScoreWinLabel.setObjectName("highScoreWinLabel")
        self.againButton = QtWidgets.QPushButton(YouWinScreen)
        self.againButton.setGeometry(QtCore.QRect(70, 250, 75, 23))
        self.againButton.setObjectName("againButton")
        self.exitGameButton = QtWidgets.QPushButton(YouWinScreen)
        self.exitGameButton.setGeometry(QtCore.QRect(240, 250, 75, 23))
        self.exitGameButton.setObjectName("exitGameButton")
        self.label = QtWidgets.QLabel(YouWinScreen)
        self.label.setGeometry(QtCore.QRect(80, 220, 271, 16))
        self.label.setObjectName("label")

        self.retranslateUi(YouWinScreen)
        QtCore.QMetaObject.connectSlotsByName(YouWinScreen)

    def retranslateUi(self, YouWinScreen):
        _translate = QtCore.QCoreApplication.translate
        YouWinScreen.setWindowTitle(_translate("YouWinScreen", "Form"))
        self.youGuessedNumberLabel.setText(_translate("YouWinScreen", "You Win!!"))
        self.scoreYouWinLabel.setText(_translate("YouWinScreen", "TextLabel"))
        self.highScoreWinLabel.setText(_translate("YouWinScreen", "TextLabel"))
        self.againButton.setText(_translate("YouWinScreen", "Play Again"))
        self.exitGameButton.setText(_translate("YouWinScreen", "Quit"))
        self.label.setText(_translate("YouWinScreen", "Play Again or Quit and choose different numbers!"))

