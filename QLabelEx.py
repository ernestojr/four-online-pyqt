# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class QLabelEx(QLabel):

    def __init(self, parent):
        QLabel.__init__(self, parent)

    def mouseReleaseEvent(self, ev):
        self.emit(SIGNAL('clicked()'))