# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lexical.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class Ui_Lexical(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(911, 656)
        self.token_table = QtWidgets.QTableWidget(Form)
        self.token_table.setGeometry(QtCore.QRect(20, 50, 411, 591))
        self.token_table.setObjectName("token_table")
        self.token_table.setColumnCount(3)
        self.token_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.token_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.token_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.token_table.setHorizontalHeaderItem(2, item)
        self.token_table.horizontalHeader().setVisible(True)
        self.token_table.verticalHeader().setVisible(False)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.infos_table = QtWidgets.QTableWidget(Form)
        self.infos_table.setGeometry(QtCore.QRect(450, 50, 441, 591))
        self.infos_table.setObjectName("infos_table")
        self.infos_table.setColumnCount(3)
        self.infos_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.infos_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.infos_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.infos_table.setHorizontalHeaderItem(2, item)
        self.infos_table.horizontalHeader().setVisible(True)
        self.infos_table.verticalHeader().setVisible(False)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(450, 20, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.token_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "input"))
        item = self.token_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "output"))
        item = self.token_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "line"))
        self.label.setText(_translate("Form", "Token序列："))
        item = self.infos_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "input"))
        item = self.infos_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "info"))
        item = self.infos_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "line"))
        self.label_3.setText(_translate("Form", "错误信息："))

class Lexical(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Lexical()
        self.ui.setupUi(self)
        self.setWindowTitle("Lexical")