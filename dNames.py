# -*- coding: utf-8 -*-

from PyQt4 import QtGui


class DNames(QtGui.QWidget):

    def __init__(self, name1, name2):
        super(DNames, self).__init__()

        self.initUI(name1, name2)

    def initUI(self, name1, name2):

        title = QtGui.QLabel('Jugador 1')
        author = QtGui.QLabel('Jugador 2')

        titleEdit = QtGui.QLineEdit(name1)
        authorEdit = QtGui.QLineEdit(name2)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        self.setLayout(grid)

        #self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Nombres de jugadores')
        self.show()