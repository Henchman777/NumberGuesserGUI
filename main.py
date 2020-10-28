import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction, QMessageBox
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import uic

from mainwindow import Ui_MainWindow
from gamescreen import Ui_GameScreen
from youwin import Ui_YouWinScreen

highScore, curScore, minNum, maxNum = 0, 0, 0, 20

class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Random Number Guesser')

        self.highScoreMain.setAlignment(Qt.AlignHCenter)
        self.highScoreMain.setText(f'High Score: {highScore}')

        self.startButton.clicked.connect(self.start_game)
        self.quitButton.clicked.connect(self.close)

        self.minNumSpinBox.valueChanged.connect(self.min_value_changed)
        self.maxNumSpinBox.valueChanged.connect(self.max_value_changed)

    @pyqtSlot()
    def start_game(self):
        global minNum
        global maxNum
        global curScore

        minNum = self.minNumSpinBox.value()
        maxNum = self.maxNumSpinBox.value()
        curScore = 0

        if minNum > maxNum:
            msg = QMessageBox()
            msg.setWindowTitle("Invalid Input")
            msg.setText("Minimum number has to be less than the maximum number.")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
            self.minNumSpinBox.setValue(0)
            self.maxNumSpinBox.setValue(20)
            return

        if minNum < -100000:
            msg = QMessageBox()
            msg.setWindowTitle("Invalid Min Number")
            msg.setText("Minimum number has to greater than -100,000.")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
            self.minNumSpinBox.setValue(0)
            self.maxNumSpinBox.setValue(20)
            return
        
        if maxNum > 100000:
            msg = QMessageBox()
            msg.setWindowTitle("Invalid Max Number")
            msg.setText("Maximum number has to less than 100,000.")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
            self.minNumSpinBox.setValue(0)
            self.maxNumSpinBox.setValue(20)
            return

        if minNum > 100000 or maxNum < -100000:
            msg = QMessageBox()
            msg.setWindowTitle("Invalid Numbers")
            msg.setText("Invalid Numbers")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
            self.minNumSpinBox.setValue(0)
            self.maxNumSpinBox.setValue(20)
            return

        global screen
        screen = GameScreen()
        return screen

    @pyqtSlot()
    def min_value_changed(self):
        minNum = self.minNumSpinBox.value()

    @pyqtSlot()
    def max_value_changed(self):
        maxNum = self.maxNumSpinBox.value()

    def you_win(self):
        pass


class GameScreen(QMainWindow, Ui_GameScreen):

    def __init__(self, *args, obj=None, **kwargs):
        super(GameScreen, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        global minNum
        global maxNum
        global highScore
        global curScore
        self.value = randint(minNum, maxNum)

        self.highScoreGame.setText(f'High Score: {highScore}')
        self.currentScore.setText(f'Current Score: {curScore}')
        self.userInputSpinBox.setValue(minNum)

        self.chooseANumberLabel.setText(f'Please choose a number between {minNum} and {maxNum}.')

        self.submitButton.clicked.connect(self.submit_guess)

    @pyqtSlot()
    def submit_guess(self):
        global minNum
        global maxNum
        global curScore
        curScore += 1
        if self.userInputSpinBox.value() < minNum or self.userInputSpinBox.value() > maxNum:
            curScore -= 1
            msg = QMessageBox()
            msg.setWindowTitle("Wrong Value")
            msg.setText("Invalid input")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
            self.userInputSpinBox.setValue(minNum)
        else:
            if self.userInputSpinBox.value() == self.value:
                self.chooseANumberLabel.setText('You Win!!')
                check_high_score()
                global youWinScreen
                youWinScreen = YouWinScreen()
                self.close()
                return youWinScreen
            elif self.userInputSpinBox.value() > self.value:
                maxNum = self.userInputSpinBox.value() - 1
                self.chooseANumberLabel.setText(f'Please choose a number between {minNum} and {maxNum}.')
                self.currentScore.setText(f'Current Score: {curScore}')
            elif self.userInputSpinBox.value() < self.value:
                minNum = self.userInputSpinBox.value() + 1
                self.chooseANumberLabel.setText(f'Please choose a number between {minNum} and {maxNum}.')
                self.currentScore.setText(f'Current Score: {curScore}')


def check_high_score():
    global curScore
    global highScore
    if curScore > highScore:
        highScore = curScore


class YouWinScreen(QMainWindow, Ui_YouWinScreen):

    def __init__(self, *args, obj=None, **kwargs):
        super(YouWinScreen, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

        global highScore
        global curScore

        self.highScoreWinLabel.setText(f'High Score: {highScore}')
        self.scoreYouWinLabel.setText(f'Your Score: {curScore}')

        self.exitGameButton.clicked.connect(self.close_window)
        self.againButton.clicked.connect(self.play_again)
    
    @pyqtSlot()
    def close_window(self):
        global win
        global highScore
        win.highScoreMain.setText(f'High Score: {highScore}')
        self.close()

    @pyqtSlot()
    def play_again(self):
        win.start_game()
        self.close()


app = QApplication(sys.argv)

win = Window()
win.show()
app.exec_()
