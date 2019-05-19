# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Semantic.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Semantic(object):
    def setupUi(self, Semantic):
        Semantic.setObjectName("Semantic")
        Semantic.resize(1392, 776)
        self.label = QtWidgets.QLabel(Semantic)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 16))
        font = QtGui.QFont()
        font.setFamily("华文宋体")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Semantic)
        self.label_2.setGeometry(QtCore.QRect(980, 20, 101, 16))
        font = QtGui.QFont()
        font.setFamily("华文宋体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.infos_table = QtWidgets.QTableWidget(Semantic)
        self.infos_table.setGeometry(QtCore.QRect(980, 50, 381, 691))
        self.infos_table.setObjectName("infos_table")
        self.infos_table.setColumnCount(3)
        self.infos_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.infos_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.infos_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.infos_table.setHorizontalHeaderItem(2, item)
        self.infos_table.verticalHeader().setVisible(False)
        self.symbol_table = QtWidgets.QTableWidget(Semantic)
        self.symbol_table.setGeometry(QtCore.QRect(570, 50, 381, 691))
        self.symbol_table.setObjectName("symbol_table")
        self.symbol_table.setColumnCount(3)
        self.symbol_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.symbol_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.symbol_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.symbol_table.setHorizontalHeaderItem(2, item)
        self.symbol_table.verticalHeader().setVisible(False)
        self.label_3 = QtWidgets.QLabel(Semantic)
        self.label_3.setGeometry(QtCore.QRect(570, 20, 101, 16))
        font = QtGui.QFont()
        font.setFamily("华文宋体")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.result_table = QtWidgets.QTableWidget(Semantic)
        self.result_table.setGeometry(QtCore.QRect(20, 50, 521, 691))
        self.result_table.setObjectName("result_table")
        self.result_table.setColumnCount(3)
        self.result_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(2, item)
        self.result_table.verticalHeader().setVisible(False)

        self.retranslateUi(Semantic)
        QtCore.QMetaObject.connectSlotsByName(Semantic)

    def retranslateUi(self, Semantic):
        _translate = QtCore.QCoreApplication.translate
        Semantic.setWindowTitle(_translate("Semantic", "Form"))
        self.label.setText(_translate("Semantic", "分析结果："))
        self.label_2.setText(_translate("Semantic", "错误："))
        item = self.infos_table.horizontalHeaderItem(0)
        item.setText(_translate("Semantic", "input"))
        item = self.infos_table.horizontalHeaderItem(1)
        item.setText(_translate("Semantic", "info"))
        item = self.infos_table.horizontalHeaderItem(2)
        item.setText(_translate("Semantic", "line"))
        item = self.symbol_table.horizontalHeaderItem(0)
        item.setText(_translate("Semantic", "name"))
        item = self.symbol_table.horizontalHeaderItem(1)
        item.setText(_translate("Semantic", "type"))
        item = self.symbol_table.horizontalHeaderItem(2)
        item.setText(_translate("Semantic", "offset"))
        self.label_3.setText(_translate("Semantic", "符号表："))
        item = self.result_table.horizontalHeaderItem(0)
        item.setText(_translate("Semantic", "序号"))
        item = self.result_table.horizontalHeaderItem(1)
        item.setText(_translate("Semantic", "三地址码"))
        item = self.result_table.horizontalHeaderItem(2)
        item.setText(_translate("Semantic", "四元式"))


from PyQt5.QtWidgets import QWidget


class Semantic(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Semantic()
        self.ui.setupUi(self)
        self.setWindowTitle("Semantic")
