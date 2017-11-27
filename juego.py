# -*- coding: utf-8 -*-
import tablero
import os


class Juego:
    def __init__(self, jugador1, jugador2, modo):
        self.__jugador1 = jugador1
        self.__jugador2 = jugador2
        self.__tablero = tablero.Tablero(6, 7)
        self.__turno = 1
        self.__modo = modo

    def getTablero(self):
        return self.__tablero.getTabla()

    def getTurno(self):
        if self.__turno == 1:
            return self.__jugador1
        else:
            return self.__jugador2

    def jugarTurno(self, col=True):
        jug = None
        if self.__turno == 1:
            jug = self.__jugador1
        else:
            jug = self.__jugador2

        result = None

        if col is True:
            result = jug.realizarJugada(self.__tablero)
        else:
            result = jug.realizarJugada(self.__tablero, col)

        print result
        print jug.getNombre()

        if result is False:
            return result

        if self.__turno == 1:
            self.__turno = 2
        else:
            self.__turno = 1

        value = self.__tablero.contarCuatroLineaH(jug.getId())
        value = value + self.__tablero.contarCuatroLineaV(jug.getId())
        value = value + self.__tablero.contarCuatroLineaD1(jug.getId())
        value = value + self.__tablero.contarCuatroLineaD2(jug.getId())

        if value > jug.getPuntaje():
            jug.setPuntaje(value)
            if self.__modo == 1:
                return jug

        if self.__modo == 2:
            fin = self.__tablero.tableroLleno()
            if fin:
                j1 = self.__jugador1.getPuntaje()
                j2 = self.__jugador2.getPuntaje()
                if j1 > j2:
                    return self.__jugador1
                elif j1 < j2:
                    return self.__jugador2
                else:
                    return 2
        if result:
            return 1

    def mostrarTabla(self):
        self.__tablero.mostrarTablero()

    def mostrarPuntos(self):
        print "Puntos:"
        print self.__jugador1.getNombre(), "-->", self.__jugador1.getPuntaje()
        print self.__jugador2.getNombre(), "-->", self.__jugador2.getPuntaje()

    def jugar(self):

        fin = False

        while(not fin):

            #Linux
            #os.system("clear")
            #Windows
            os.system("cls")
            jug = None
            if self.__turno == 1:
                jug = self.__jugador1
                self.__turno = 2
            else:
                jug = self.__jugador2
                self.__turno = 1

            self.__tablero.mostrarTablero()
            self.mostrarPuntos()

            #jug.getListaPosibles(self.__tablero)

            if jug.realizarJugada(self.__tablero) is False:
                print "El jugador ", jug.getNombre(), " se ha retirado"
                print "Felicidades al Ganador"
                print "Fin del Juego"
                break

            value = self.__tablero.contarCuatroLineaH(jug.getId())
            value = value + self.__tablero.contarCuatroLineaV(jug.getId())
            value = value + self.__tablero.contarCuatroLineaD1(jug.getId())
            value = value + self.__tablero.contarCuatroLineaD2(jug.getId())

            if value > jug.getPuntaje():
                jug.setPuntaje(value)
                if self.__modo == 1:
                    fin = True
                    self.__tablero.mostrarTablero()
                    self.mostrarPuntos()
                    print "Fin del juego\nGanador: ", jug.getNombre()
                    continue

            if self.__modo == 2:
                fin = self.__tablero.tableroLleno()
                if fin:
                    self.__tablero.mostrarTablero()
                    self.mostrarPuntos()
                    j1 = self.__jugador1.getPuntaje()
                    j2 = self.__jugador2.getPuntaje()
                    if j1 > j2:
                        print "Fin del juego"
                        print "Ganador: ", self.__jugador1.getNombre()
                        print "Puntos: ", self.__jugador1.getPuntaje()
                    elif j1 < j2:
                        print "Fin del juego"
                        print "Ganador: ", self.__jugador2.getNombre()
                        print "Puntos: ", self.__jugador2.getPuntaje()
                    else:
                        print "Fin del juego"
                        print "Juego Empatado"
                        print "Puntajes:"
                        print  self.__jugador1.getNombre()
                        print "Puntos: ", self.__jugador1.getPuntaje()
                        print  self.__jugador2.getNombre()
                        print "Puntos: ", self.__jugador2.getPuntaje()