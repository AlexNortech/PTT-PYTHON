import sys
from img import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import random


class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("inicio.ui", self)
        self.frame.mouseMoveEvent = self.moveWindow
        self.salir.clicked.connect(self.exit)
        self.min.clicked.connect(self.minimizar)
        self.jugar.clicked.connect(self.window_access)

    def exit(self):
        app.exit()
        sys.exit()

    def moveWindow(self, e):
        if e.buttons() == Qt.LeftButton:
            self.move(self.pos() + e.globalPos() - self.clickPosition)
            self.clickPosition = e.globalPos()
            e.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def minimizar(self):
        widget.showMinimized()

    def window_access(self):
        ventana_2 = Gui_Juego()
        widget.addWidget(ventana_2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(768)
        widget.setFixedWidth(1366)


class Gui_Juego(QMainWindow):
    def __init__(self):
        super(Gui_Juego, self).__init__()
        loadUi("juego.ui", self)
        self.frame.mouseMoveEvent = self.moveWindow
        self.salir.clicked.connect(self.exit)
        self.min.clicked.connect(self.minimizar)
        self.piedra.clicked.connect(self.img_piedra)
        self.papel.clicked.connect(self.img_papel)
        self.tijera.clicked.connect(self.img_tijera)

    def exit(self):
        app.exit()
        sys.exit()

    def moveWindow(self, e):
        if e.buttons() == Qt.LeftButton:
            self.move(self.pos() + e.globalPos() - self.clickPosition)
            self.clickPosition = e.globalPos()
            e.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def minimizar(self):
        widget.showMinimized()

    def img_piedra(self):
        self.label_yo.setStyleSheet("border-image: url(:/imagenes/piedra.png);")
        self.computadora()
        if self.decision_computadora == 0:
            self.label_msg.setStyleSheet('color: pink;'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Empate!")
        elif self.decision_computadora == 1:
            self.label_msg.setStyleSheet('color: red;'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Pierdes...")
        else:
            self.label_msg.setStyleSheet('color: rgb(85, 255, 0);'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Ganaste!")

    def img_papel(self):
        self.label_yo.setStyleSheet("border-image: url(:/imagenes/papel.png);")
        self.computadora()
        if self.decision_computadora == 0:
            self.label_msg.setStyleSheet('color: rgb(85, 255, 0);'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Ganaste")
        elif self.decision_computadora == 1:
            self.label_msg.setStyleSheet('color: pink;'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Empate!")
        else:
            self.label_msg.setStyleSheet('color: red;'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Perdiste...")

    def img_tijera(self):
        self.label_yo.setStyleSheet("border-image: url(:/imagenes/tijera.png);")
        self.computadora()
        if self.decision_computadora == 0:
            self.label_msg.setStyleSheet('color: red;'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Pierdes...")
        elif self.decision_computadora == 1:
            self.label_msg.setStyleSheet('color: rgb(85, 255, 0);'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Ganaste!")
        else:
            self.label_msg.setStyleSheet('color: pink;'
                                         'background-color: rgba(120,120,120,100);'
                                         'font: 30pt "Britannic Bold";')
            self.label_msg.setText("Empate!")


    def computadora(self):
        self.decision_computadora = random.randint(0, 2)
        if self.decision_computadora == 0:
            self.label_computadora.setStyleSheet("border-image: url(:/imagenes/piedra.png);")
        elif self.decision_computadora == 1:
            self.label_computadora.setStyleSheet("border-image: url(:/imagenes/papel.png);")
        else:
            self.label_computadora.setStyleSheet("border-image: url(:/imagenes/tijera.png);")


# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(768)
widget.setFixedWidth(1366)
widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Saliendo")