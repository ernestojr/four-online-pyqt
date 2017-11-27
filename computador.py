# -*- coding: utf-8 -*-
import random
import jugador


class Computadora(jugador.Jugador):
    def __init__(self, nombre, _id, _idRival):
        jugador.Jugador.__init__(self, nombre, _id)
        self.__idRival = _idRival

    def getListaPos(self, tabla, _id):
        lista = tabla.contarCuatroLineaH(_id, True)
        listaV = tabla.contarCuatroLineaV(_id, True)
        if len(listaV) > 0:
            for i in range(len(listaV)):
                lista.append(listaV[i])
        listaD1 = tabla.contarCuatroLineaD1(_id, True)
        if len(listaD1) > 0:
            for i in range(len(listaD1)):
                lista.append(listaD1[i])
        listaD2 = tabla.contarCuatroLineaD2(_id, True)
        if len(listaD2) > 0:
            for i in range(len(listaD2)):
                lista.append(listaD2[i])
        return lista

    def realizarJugada(self, tablero):
        result = False
        col = 0
        while not result:

            lista = self.getListaPos(tablero, self.getId())
            if len(lista):
                col = lista[random.randrange(len(lista))]
            else:
                lista = self.getListaPos(tablero, self.__idRival)
                if len(lista):
                    col = lista[random.randrange(len(lista))]
                    print "** ", col
                else:
                    col = random.randrange(7)

            result = tablero.agregarFicha(self, col)
        print self.getNombre()
        print "=> ", col
        return True