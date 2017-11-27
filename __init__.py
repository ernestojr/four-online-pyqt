# -*- coding: utf-8 -*-

import WidgetCL
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Ventana(QMainWindow):

    def __init__(self):
        super(Ventana, self).__init__()
        self.__modo = 2
        self.__tipo = 0

        self.initUI()

    def initUI(self):

        self.__widget = WidgetCL.WidgetCL(self.__modo, self.__tipo)
        self.setCentralWidget(self.__widget)

        newAction = QAction(QIcon('image/new.png'), 'Nuevo', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('Juego Nuevo')
        newAction.triggered.connect(self.nuevo)

        exitAction = QAction(QIcon('image/cross.png'), 'Salir', self)
        exitAction.setShortcut('Ctrl+S')
        exitAction.setStatusTip('Salir del Juego')
        exitAction.triggered.connect(self.close)

        humVsHumAction = QAction(QIcon('image/humvshum.png'),
            'Humano Vs Humano', self)
        humVsHumAction.setShortcut('Ctrl+H')
        humVsHumAction.setStatusTip('Humano Vs Humano')
        humVsHumAction.triggered.connect(self.humVsHum)

        humVsCpuAction = QAction(QIcon('image/humvscpu.png'),
            'Humano Vs Computadora', self)
        humVsCpuAction.setShortcut('Ctrl+J')
        humVsCpuAction.setStatusTip('Humano Vs Computadora')
        humVsCpuAction.triggered.connect(self.humVsCpu)

        cpuVsCpuAction = QAction(QIcon('image/cpuvscpu.png'),
            'Computadora Vs Computadora', self)
        cpuVsCpuAction.setShortcut('Ctrl+C')
        cpuVsCpuAction.setStatusTip('Computadora Vs Computadora')
        cpuVsCpuAction.triggered.connect(self.cpuVsCpu)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Archivo')
        fileMenu.addAction(newAction)
        fileMenu.addAction(exitAction)
        gameMenu = menubar.addMenu('Juego')
        gameMenu.addAction(humVsHumAction)
        gameMenu.addAction(humVsCpuAction)
        gameMenu.addAction(cpuVsCpuAction)

        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(newAction)
        toolbar.addAction(humVsHumAction)
        toolbar.addAction(humVsCpuAction)
        toolbar.addAction(cpuVsCpuAction)
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 0, 0)
        self.setWindowTitle('Cuatro en linea')
        #self.show()

    def nuevo(self):
        if self.__widget.getEdoJuego():
                reply = QMessageBox.question(self, 'Mensaje',
                    "Seguro que desea generar un juego nuevo?\n"
                    + "Se perderan la partida actual", "Aceptar",
                    "Cancel")
                if reply != 0:
                    return
        self.__widget.setTipoJuego(self.__tipo)

    def humVsHum(self):
        print "Hola mundo"
        if self.__tipo != 0:
            if self.__widget.getEdoJuego():
                reply = QMessageBox.question(self, 'Mensaje',
                    "Seguro que desea cambiar la categoria de juego?\n"
                    + "Se perderan la partida actual", "Aceptar",
                    "Cancel")
                if reply != 0:
                    return
            self.__widget.setCTitle("Humano Vs Humano")
            self.__widget.setTipoJuego(0)
            self.__tipo = 0

    def humVsCpu(self):
        print "Hola mundo"
        if self.__tipo != 1:
            if self.__widget.getEdoJuego():
                reply = QMessageBox.question(self, 'Mensaje',
                    "Seguro que desea cambiar la categoria de juego?\n"
                    + "Se perderan la partida actual", "Aceptar",
                    "Cancel")
                if reply != 0:
                    return
            self.__widget.setCTitle("Humano Vs Computadora")
            self.__widget.setTipoJuego(1)
            self.__tipo = 1

    def cpuVsCpu(self):
        print "Hola mundo"
        if self.__tipo != 2:
            if self.__widget.getEdoJuego():
                reply = QMessageBox.question(self, 'Mensaje',
                    "Seguro que desea cambiar la categoria de juego?\n"
                    + "Se perderan la partida actual", "Aceptar",
                    "Cancel")
                if reply != 0:
                    return
            self.__widget.setCTitle("Computadora Vs Computadora")
            self.__widget.setTipoJuego(2)
            self.__tipo = 2

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Mensaje',
            "Seguro que desea salir de Cuatro en Linea?", "Aceptar",
            "Cancel")
        if reply == 0:
            event.accept()
        else:
            event.ignore()

        self.statusBar()


def main():

    app = QApplication(sys.argv)
    ex = Ventana()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()