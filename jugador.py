# -*- coding: utf-8 -*-


class Jugador:
    def __init__(self, nombre, _id):
        self.__nombre = nombre
        self.__puntaje = 0
        self.__id = _id

    def getNombre(self):
        return self.__nombre

    def getPuntaje(self):
        return self.__puntaje

    def setPuntaje(self, value):
        self.__puntaje = value

    def getId(self):
        return self.__id

    def getListaPosibles(self, tabla):
        listaH = tabla.contarCuatroLineaH(self.__id, True)
        if len(listaH) > 0:
            cadena = self.__nombre + " H => "
            for i in range(len(listaH)):
                cadena = cadena + str(listaH[i]) + " "
            print cadena
        listaV = tabla.contarCuatroLineaV(self.__id, True)
        if len(listaV) > 0:
            cadena = self.__nombre + " V => "
            for i in range(len(listaV)):
                cadena = cadena + str(listaV[i]) + " "
            print cadena
        listaD1 = tabla.contarCuatroLineaD1(self.__id, True)
        if len(listaD1) > 0:
            cadena = self.__nombre + " D1 => "
            for i in range(len(listaD1)):
                cadena = cadena + str(listaD1[i]) + " "
            print cadena
        listaD2 = tabla.contarCuatroLineaD2(self.__id, True)
        if len(listaD2) > 0:
            cadena = self.__nombre + " D2 => "
            for i in range(len(listaD2)):
                cadena = cadena + str(listaD2[i]) + " "
            print cadena

    def realizarJugada(self, tablero, col=None):
        if col is not None:
            return tablero.agregarFicha(self, col)
        result = False
        while not result:
            col = 0

            while True:
                try:
                    print self.__nombre
                    print "Ingrese el número la columna [0-6]. Salir: -1"
                    print "El valor ingresado no debe ser menor a 0."
                    col = raw_input("=> ")
                    col = int(col)
                    if col > 6:
                        print "El valor ingresado no debe ser mayor a 5."
                        continue
                    if col < 0:
                        return False
                except ValueError:
                    print "El valor ingresado no es un numero. Intente de nuevo"
                    continue
                break
            result = tablero.agregarFicha(self, col)
            if not result:
                    print "La columna ingresada esta llena. Intente con otra"
        return True