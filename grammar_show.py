# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grammar_show.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget


class Ui_Grammar(object):
    def setupUi(self, Grammar):
        Grammar.setObjectName("Grammar")
        Grammar.resize(1651, 752)
        self.Forcast_Table = QtWidgets.QTableWidget(Grammar)
        self.Forcast_Table.setGeometry(QtCore.QRect(20, 30, 691, 701))
        self.Forcast_Table.setObjectName("Forcast_Table")
        self.Forcast_Table.setColumnCount(0)
        self.Forcast_Table.setRowCount(0)
        self.FF_Table = QtWidgets.QTableWidget(Grammar)
        self.FF_Table.setGeometry(QtCore.QRect(740, 30, 491, 701))
        self.FF_Table.setObjectName("FF_Table")
        self.FF_Table.setColumnCount(2)
        self.FF_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.FF_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.FF_Table.setHorizontalHeaderItem(1, item)
        self.Select_Table = QtWidgets.QTableWidget(Grammar)
        self.Select_Table.setGeometry(QtCore.QRect(1260, 30, 371, 701))
        self.Select_Table.setObjectName("Select_Table")
        self.Select_Table.setColumnCount(2)
        self.Select_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Select_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Select_Table.setHorizontalHeaderItem(1, item)

        self.retranslateUi(Grammar)
        QtCore.QMetaObject.connectSlotsByName(Grammar)

    def retranslateUi(self, Grammar):
        _translate = QtCore.QCoreApplication.translate
        Grammar.setWindowTitle(_translate("Grammar", "Form"))
        item = self.FF_Table.horizontalHeaderItem(0)
        item.setText(_translate("Grammar", "First"))
        item = self.FF_Table.horizontalHeaderItem(1)
        item.setText(_translate("Grammar", "Follow"))
        item = self.Select_Table.horizontalHeaderItem(0)
        item.setText(_translate("Grammar", "产生式"))
        item = self.Select_Table.horizontalHeaderItem(1)
        item.setText(_translate("Grammar", "Select"))


class Grammar_Show(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Grammar()
        self.ui.setupUi(self)
        self.setWindowTitle("Grammar")
