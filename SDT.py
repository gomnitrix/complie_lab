# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SDT.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SDT(object):
    def setupUi(self, SDT):
        SDT.setObjectName("SDT")
        SDT.resize(974, 855)
        self.SDT_Table = QtWidgets.QTableWidget(SDT)
        self.SDT_Table.setGeometry(QtCore.QRect(10, 10, 951, 831))
        self.SDT_Table.setObjectName("SDT_Table")
        self.SDT_Table.setColumnCount(0)
        self.SDT_Table.setRowCount(0)

        self.retranslateUi(SDT)
        QtCore.QMetaObject.connectSlotsByName(SDT)

    def retranslateUi(self, SDT):
        _translate = QtCore.QCoreApplication.translate
        SDT.setWindowTitle(_translate("SDT", "Form"))


from PyQt5.QtWidgets import QWidget


class SDTShow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_SDT()
        self.ui.setupUi(self)
        self.setWindowTitle("SDT")