# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        #for i in range(10):
            #layout.addWidget(QImage("facebook.png"))
        #icon = QIcon()
        #layout.addWidget(QLabel("Hola mundo"))
        #layout.addWidget(QCheckBox("Uno"))
        #layout.addWidget(QCheckBox("Dos"))
        #layout.addWidget(QLineEdit())
        #layout.addWidget(QPushButton("Aceptar"))
        self.setLayout(layout)
        self.setWindowIcon(QIcon("facebook.png"))
        self.setWindowIconText("Prueba")


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
