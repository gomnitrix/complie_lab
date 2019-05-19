# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grammar_analyze.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Grammar_Analyze(object):
    def setupUi(self, Grammar_Analyze):
        Grammar_Analyze.setObjectName("Grammar_Analyze")
        Grammar_Analyze.resize(1368, 755)
        self.treeWidget = QtWidgets.QTreeWidget(Grammar_Analyze)
        self.treeWidget.setGeometry(QtCore.QRect(20, 50, 871, 691))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.infos_table = QtWidgets.QTableWidget(Grammar_Analyze)
        self.infos_table.setGeometry(QtCore.QRect(910, 50, 441, 691))
        self.infos_table.setObjectName("infos_table")
        self.infos_table.setColumnCount(3)
        self.infos_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.infos_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.infos_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.infos_table.setHorizontalHeaderItem(2, item)
        self.label = QtWidgets.QLabel(Grammar_Analyze)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 16))
        font = QtGui.QFont()
        font.setFamily("华文宋体")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Grammar_Analyze)
        self.label_2.setGeometry(QtCore.QRect(910, 20, 101, 16))
        font = QtGui.QFont()
        font.setFamily("华文宋体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Grammar_Analyze)
        QtCore.QMetaObject.connectSlotsByName(Grammar_Analyze)

    def retranslateUi(self, Grammar_Analyze):
        _translate = QtCore.QCoreApplication.translate
        Grammar_Analyze.setWindowTitle(_translate("Grammar_Analyze", "Form"))
        item = self.infos_table.horizontalHeaderItem(0)
        item.setText(_translate("Grammar_Analyze", "input"))
        item = self.infos_table.horizontalHeaderItem(1)
        item.setText(_translate("Grammar_Analyze", "info"))
        item = self.infos_table.horizontalHeaderItem(2)
        item.setText(_translate("Grammar_Analyze", "line"))
        self.label.setText(_translate("Grammar_Analyze", "语法分析树："))
        self.label_2.setText(_translate("Grammar_Analyze", "错误："))


from PyQt5.QtWidgets import QWidget


class GrammarAnalyze(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Grammar_Analyze()
        self.ui.setupUi(self)
        self.setWindowTitle("Grammar")
