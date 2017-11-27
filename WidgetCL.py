# -*- coding: utf-8 -*-
import QLabelEx
import dNames
import jugador
import juego
import computador
#import time
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class WidgetCL(QWidget):

    def __init__(self, modo, tipo):
        super(WidgetCL, self).__init__()

        self.__nombre1 = "Ernesto"
        self.__nombre2 = "Kenny"
        self.__imageNone = "image/default.png"
        self.__imageJ1 = "image/face.png"
        self.__imageJ2 = "image/twit.png"
        self.__tipo = tipo
        self.__modo = modo
        self.initUI()
        self.inicializar()

    def getEdoJuego(self):
        return self.__inicio

    def initUI(self):

        grid = QGridLayout()
        self.__labels = []
        for i in range(6):
            self.__labels.append([])
            for j in range(7):
                label = QLabelEx.QLabelEx()
                #label.setPixmap(QPixmap(self.__imageNone))
                self.connect(label, SIGNAL('clicked()'), self.buttonClicked)
                grid.addWidget(label, i, j)
                self.__labels[i].append(label)

        f = QFont("Roboto", 30, QFont.Light)
        self.__title = QLabel("Humano Vs Humano")
        self.__title.setFont(f)
        self.__title.setAlignment(Qt.AlignHCenter)

        sf = QFont("Roboto-Italic", 20)
        self.__subTitle = QLabelEx.QLabelEx("0 - Pedro Vs Juan - 0")
        self.__subTitle.setFont(sf)
        self.__subTitle.setAlignment(Qt.AlignHCenter)
        self.connect(self.__subTitle, SIGNAL('clicked()'), self.buttonClicked)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.__title)
        vbox.addWidget(self.__subTitle)
        vbox.addLayout(grid)

        self.setLayout(vbox)

        self.move(300, 150)
        self.setWindowTitle('Cuatro en linea')

    def calcularColumna(self, _id):
        for i in range(6):
            for j in range(7):
                if(id(self.__labels[i][j]) == _id):
                    return j
        return False

    def buttonClicked(self):
        sender = self.sender()
        if id(sender) == id(self.__subTitle):
            self.__names = dNames.DNames(self.__nombre1, self.__nombre2)
            self.__names.show()
            return
        if self.__tipo == 0:
            self.__inicio = True
            if self.__block is False:
                self.__block = True
                self.jugada(self.calcularColumna(id(sender)))
        elif self.__tipo == 1:
            self.__inicio = True
            if self.__block is False:
                self.__block = True
                self.jugada(self.calcularColumna(id(sender)))

    def jugada(self, col):
        result = self.__juego.jugarTurno(col)
        self.actualizarTabla()
        if self.evaluarResult(result):
            if self.__tipo == 1:
                result = self.__juego.jugarTurno()
                self.actualizarTabla()
                if self.evaluarResult(result) is False:
                    return
            self.__block = False

    def evaluarResult(self, result):
        if result is False:
            QMessageBox.information(self, 'Mensaje',
                    "La columna seleccionada esta llena", "Aceptar")
            print "Columna llena"
            self.__block = False
            return False
        elif result == 1:
            print "Jugada valida"
            return True
        elif result == 2:
            cad = "Fin del Juego\nEmpatados!\n" + self.__judador1.getNombre()
            cad = cad + " -> " + str(
                self.__judador1.getPuntaje()) + " puntos.\n"
            cad = cad + self.__judador2.getNombre() + " -> " + str(
                self.__judador2.getPuntaje()) + " puntos."
            QMessageBox.information(self, 'Mensaje',
                    cad, "Aceptar")
            return False
        else:
            cad = "Fin del Juego\nGanador: " + result.getNombre()
            cad = cad + "\nPuntos: " + str(result.getPuntaje())
            QMessageBox.information(self, 'Mensaje',
                    cad, "Aceptar")
            return False

    def setCTitle(self, title):
        self.__title.setText(title)

    def setCSubTitle(self, value):
        self.__subTitle.setText(value)

    def jugadaAuto(self):
        self.__block = True
        while True:
            result = self.__juego.jugarTurno()
            self.actualizarTabla()
            #time.sleep(1)
            if self.evaluarResult(result) is False:
                return

    def setTipoJuego(self, tipo):
        self.__tipo = tipo
        self.inicializar()
        if self.__tipo == 2:
            result = QMessageBox.information(self, 'Mensaje',
                    "Cuando quiera empezar la partida presione Iniciar",
                    "Iniciar")
            if result == 0:
                self.jugadaAuto()

    def inicializar(self):
        self.__inicio = False
        self.__block = False
        for i in range(6):
            for j in range(7):
                self.__labels[i][j].setPixmap(QPixmap(self.__imageNone))
        if self.__tipo == 0:
            #Humano Vs Humano
            self.__judador1 = jugador.Jugador(self.__nombre1, "1")
            self.__judador2 = jugador.Jugador(self.__nombre2, "2")
        elif self.__tipo == 1:
            #Humano Vs Computadora
            #self.__nombre2 = "Computadora"
            self.__judador1 = jugador.Jugador(self.__nombre1, "1")
            self.__judador2 = computador.Computadora(self.__nombre2, "2", "1")
        else:
            #Computadora Vs Computadora
            #self.__nombre1 = "Computadora 1"
            #self.__nombre2 = "Computadora 2"
            self.__judador1 = computador.Computadora(self.__nombre1, "1", "2")
            self.__judador2 = computador.Computadora(self.__nombre2, "2", "1")
        self.__juego = juego.Juego(self.__judador1,
            self.__judador2, self.__modo)
        self.__estados = []
        for i in range(6):
            self.__estados.append([])
            for j in range(7):
                self.__estados[i].append(None)
        self.__tablaJuego = self.__juego.getTablero()
        self.__juego.mostrarTabla()
        self.actualizarPuntos()

    def actualizarPuntos(self):
        cadena = str(self.__judador1.getPuntaje())
        cadena = cadena + " - " + self.__judador1.getNombre() + " Vs "
        cadena = cadena + self.__judador2.getNombre() + " - "
        cadena = cadena + str(self.__judador2.getPuntaje())
        self.__subTitle.setText(cadena)

    def actualizarTabla(self):
        self.actualizarPuntos()
        for i in range(6):
            for j in range(7):
                if self.__tablaJuego[i][j] is not None:
                    if self.__tablaJuego[i][j] == self.__judador1.getId():
                        if self.__estados[i][j] is None:
                            self.__estados[i][j] = True
                            self.__labels[i][j].setPixmap(
                                QPixmap(self.__imageJ1))
                    else:
                        if self.__estados[i][j] is None:
                            self.__estados[i][j] = True
                            self.__labels[i][j].setPixmap(
                                QPixmap(self.__imageJ2))