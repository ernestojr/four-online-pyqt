# -*- coding: utf-8 -*-


class Tablero:
    def __init__(self, fil, col):
        self.__fil = fil
        self.__col = col
        self.__tabla = []
        for i in range(fil):
            self.__tabla.append([])
            for j in range(col):
                self.__tabla[i].append(None)

    def getTabla(self):
        return self.__tabla

    def contarCuatroLineaV(self, _id, edo=False):
        count = 0
        lista = []
        num = 4
        if edo:
            num = 3
        for j in range(self.__col):
            for i in range(self.__fil):
                if self.__tabla[i][j] == _id:
                    aux = i
                    cont = 0
                    if edo:
                        posI = i
                    state = False
                    while aux < self.__fil:
                        if self.__tabla[aux][j] == _id:
                            cont = cont + 1
                        else:
                            break
                        aux = aux + 1
                        if cont == num:
                            state = True
                            break
                    if state:
                        if edo:
                            if (posI - 1) >= 0:
                                if self.__tabla[posI - 1][j] is None:
                                    if aux < self.__fil:
                                        if self.__tabla[aux][j] == _id:
                                            break
                                    lista.append(j)
                        else:
                            count = count + 1
                        break
                    i = aux
        if edo is True:
            return lista
        else:
            return count

    def contarCuatroLineaH(self, _id, edo=False):
        count = 0
        num = 4
        lista = []
        if edo:
            num = 3
        for i in range(self.__fil):
            for j in range(self.__col):
                if self.__tabla[i][j] == _id:
                    aux = j
                    cont = 0
                    state = False
                    if edo:
                        posJ = j - 1
                        pos = -1
                    while aux < self.__col:
                        if self.__tabla[i][aux] == _id:
                            cont = cont + 1
                        else:
                            if edo:
                                if self.__tabla[i][aux] is None:
                                    if(aux + 1) < self.__col:
                                        if self.__tabla[i][aux + 1] == _id:
                                            pos = aux
                                            aux = aux + 1
                                            continue
                            break
                        aux = aux + 1
                        if cont == num:
                            state = True
                            break
                    if state:
                        if edo:
                            if pos != -1:
                                lista.append(pos)
                                break
                            if posJ >= 0:
                                if self.__tabla[i][posJ] is None:
                                    flag = True
                                    if (i + 1) < self.__fil:
                                        if self.__tabla[i + 1][posJ] is None:
                                            flag = False
                                    if flag:
                                        lista.append(posJ)
                            if aux < self.__col:
                                if self.__tabla[i][aux] is None:
                                    if (i + 1) < self.__fil:
                                        if self.__tabla[i + 1][aux] is None:
                                            break
                                    lista.append(aux)
                        else:
                            count = count + 1
                        break
                    j = aux
        if edo:
            return lista
        else:
            return count

    def __contarCuatroLineaD1_1(self, _id, edo=False):
        count = 0
        num = 4
        lista = []
        if edo:
            num = 3
        for i in range(self.__fil - 3):
            aux = i
            for j in range(self.__col - num):
                if aux == (self.__fil - num):
                    if self.__tabla[aux][j] != _id:
                        break
                if self.__tabla[aux][j] == _id:
                    ai = aux
                    aj = j
                    state = False
                    cont = 0
                    if edo:
                        posI = aux - 1
                        posJ = j - 1
                        pos = -1
                    while ai < self.__fil:
                        if self.__tabla[ai][aj] == _id:
                            cont = cont + 1
                        else:
                            if edo:
                                if self.__tabla[ai][aj] is None:
                                    ai = ai + 1
                                    aj = aj + 1
                                    if(ai < self.__fil) and (aj < self.__col):
                                        if self.__tabla[ai][aj] == _id:
                                            pos = aj - 1
                                            continue
                            break
                        ai = ai + 1
                        aj = aj + 1
                        if cont == num:
                            state = True
                            break
                    if state:
                        if edo:
                            if pos != -1:
                                lista.append(pos)
                                break
                            if (posI >= 0) and (posJ >= 0):
                                if self.__tabla[posI][posJ] is None:
                                    flag = True
                                    if self.__tabla[posI + 1][posJ] is None:
                                        flag = False
                                    if flag:
                                        lista.append(posJ)
                            if (ai < self.__fil) and (aj < self.__col):
                                if self.__tabla[ai][aj] is None:
                                    if (ai + 1) < self.__fil:
                                        if self.__tabla[ai + 1][aj] is None:
                                            break
                                    lista.append(aj)
                        else:
                            count = count + 1
                        break
                aux = aux + 1
        if edo:
            return lista
        else:
            return count

    def __contarCuatroLineaD1_2(self, _id, edo=False):
        count = 0
        num = 4
        lista = []
        if edo:
            num = 3
        for j in range(self.__col - 3):
            aux = j
            if j == 0:
                continue
            for i in range(self.__fil - 3):
                if aux == (self.__col - num):
                    if self.__tabla[i][aux] != _id:
                        break
                if self.__tabla[i][aux] == _id:
                    ai = i
                    aj = aux
                    cont = 0
                    state = False
                    if edo:
                        posI = i - 1
                        posJ = aux - 1
                        pos = -1
                    while aj < self.__col:
                        if self.__tabla[ai][aj] == _id:
                            cont = cont + 1
                        else:
                            if edo:
                                if self.__tabla[ai][aj] is None:
                                    ai = ai + 1
                                    aj = aj + 1
                                    if(ai < self.__fil) and (aj < self.__col):
                                        if self.__tabla[ai][aj] == _id:
                                            pos = aj - 1
                                            continue
                            break
                        ai = ai + 1
                        aj = aj + 1
                        if cont == num:
                            state = True
                            break
                    if state:
                        if edo:
                            if pos != -1:
                                lista.append(pos)
                                break
                            if (posI >= 0) and (posJ >= 0):
                                if self.__tabla[posI][posJ] is None:
                                    flag = True
                                    if self.__tabla[posI + 1][posJ] is None:
                                        flag = False
                                    if flag:
                                        lista.append(posJ)
                            if (ai < self.__fil) and (aj < self.__col):
                                if self.__tabla[ai][aj] is None:
                                    if (ai + 1) < self.__fil:
                                        if self.__tabla[ai + 1][aj] is None:
                                            break
                                    lista.append(aj)
                        else:
                            count = count + 1
                        break
                aux = aux + 1
        if edo:
            return lista
        else:
            return count

    def __contarCuatroLineaD2_1(self, _id, edo=False):
        count = 0
        num = 4
        lista = []
        if edo:
            num = 3
        for i in range(self.__fil - 3):
            j = self.__col - 1
            aux = i
            while aux < self.__fil:
                if self.__tabla[aux][j] == _id:
                    ai = aux
                    aj = j
                    cont = 0
                    state = False
                    if edo:
                        posI = aux - 1
                        posJ = j + 1
                        pos = -1
                    while ai < self.__fil:
                        if self.__tabla[ai][aj] == _id:
                            cont = cont + 1
                        else:
                            if edo:
                                if self.__tabla[ai][aj] is None:
                                    ai = ai + 1
                                    aj = aj - 1
                                    if(ai < self.__fil) and (aj >= 0):
                                        if self.__tabla[ai][aj] == _id:
                                            pos = aj + 1
                                            continue
                            break
                        ai = ai + 1
                        aj = aj - 1
                        if cont == num:
                            state = True
                            break
                    if state:
                        if edo:
                            if pos != -1:
                                lista.append(pos)
                                break
                            if (posI >= 0) and (posJ < self.__col):
                                if self.__tabla[posI][posJ] is None:
                                    flag = True
                                    if self.__tabla[posI + 1][posJ] is None:
                                        flag = False
                                    if flag:
                                        lista.append(posJ)
                            if (ai < self.__fil) and (aj >= 0):
                                if self.__tabla[ai][aj] is None:
                                    if (ai + 1) < self.__fil:
                                        if self.__tabla[ai + 1][aj] is None:
                                            break
                                    lista.append(aj)
                        else:
                            count = count + 1
                        break
                j = j - 1
                aux = aux + 1
        if edo:
            return lista
        else:
            return count

    def __contarCuatroLineaD2_2(self, _id, edo=False):
        count = 0
        j = self.__col - 2
        num = 4
        lista = []
        if edo:
            num = 3
        while (j >= 3):
            i = 0
            aux = j
            while (aux >= 0) and (i < self.__fil):
                if self.__tabla[i][aux] == _id:
                    cont = 0
                    ai = i
                    aj = aux
                    state = False
                    if edo:
                        posI = aux - 1
                        posJ = j + 1
                        pos = -1
                    while aj >= 0:
                        if self.__tabla[ai][aj] == _id:
                            cont = cont + 1
                        else:
                            if edo:
                                if self.__tabla[ai][aj] is None:
                                    ai = ai + 1
                                    aj = aj - 1
                                    if(ai < self.__fil) and (aj >= 0):
                                        if self.__tabla[ai][aj] == _id:
                                            pos = aj + 1
                                            continue
                            break
                        ai = ai + 1
                        aj = aj - 1
                        if cont == num:
                            state = True
                            break
                    if state:
                        if edo:
                            if pos != -1:
                                lista.append(pos)
                                break
                            if (posI >= 0) and (posJ < self.__col):
                                if self.__tabla[posI][posJ] is None:
                                    flag = True
                                    if self.__tabla[posI + 1][posJ] is None:
                                        flag = False
                                    if flag:
                                        lista.append(posJ)
                            if (ai < self.__fil) and (aj >= 0):
                                if self.__tabla[ai][aj] is None:
                                    if (ai + 1) < self.__fil:
                                        if self.__tabla[ai + 1][aj] is None:
                                            break
                                    lista.append(aj)
                        else:
                            count = count + 1
                        break
                aux = aux - 1
                i = i + 1
            j = j - 1
        if edo:
            return lista
        else:
            return count

    def contarCuatroLineaD1(self, _id, state=False):
        value = None
        if state:
            value = self.__contarCuatroLineaD1_1(_id, state)
            lista = self.__contarCuatroLineaD1_2(_id, state)
            for i in range(len(lista)):
                value.append(lista[i])
        else:
            value = self.__contarCuatroLineaD1_1(_id)
            value = value + self.__contarCuatroLineaD1_2(_id)
        return value

    def contarCuatroLineaD2(self, jugador, state=False):
        value = None
        if state:
            value = self.__contarCuatroLineaD2_1(jugador, state)
            lista = self.__contarCuatroLineaD2_2(jugador, state)
            for i in range(len(lista)):
                value.append(lista[i])
        else:
            value = self.__contarCuatroLineaD2_1(jugador)
            value = value + self.__contarCuatroLineaD2_2(jugador)
        return value

    def __obtenerPosLibre(self, col):
        i = self.__fil - 1
        while i >= 0:
            if self.__tabla[i][col] is None:
                return i
            i = i - 1
        return False

    def agregarFicha(self, jugador, col):
        pos = self.__obtenerPosLibre(col)
        if pos is False:
            return False
        self.__tabla[pos][col] = jugador. getId()
        return True

    def llenarTablero(self):
        for i in range(self.__fil):
            for j in range(self.__col):
                self.__tabla[i][j] = "1"

    def tableroLleno(self):
        for i in range(self.__fil):
            for j in range(self.__col):
                if self.__tabla[i][j] is None:
                    return False
        return True

    def mostrarTablero(self):
        for i in range(self.__fil):
            linea = ""
            for j in range(self.__col):
                value = self.__tabla[i][j]
                if value is None:
                    value = "_"
                linea = linea + "[" + value + "]"
            print linea