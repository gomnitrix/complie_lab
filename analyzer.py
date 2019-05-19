# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyzer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 828)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cf_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cf_btn.setGeometry(QtCore.QRect(720, 350, 93, 28))
        self.cf_btn.setObjectName("cf_btn")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(690, 290, 161, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lexical_rule_btn = QtWidgets.QPushButton(self.centralwidget)
        self.lexical_rule_btn.setGeometry(QtCore.QRect(720, 80, 93, 28))
        self.lexical_rule_btn.setObjectName("lexical_rule_btn")
        self.grammar_rules_btn = QtWidgets.QPushButton(self.centralwidget)
        self.grammar_rules_btn.setGeometry(QtCore.QRect(720, 150, 93, 28))
        self.grammar_rules_btn.setObjectName("grammar_rules_btn")
        self.yf_btn = QtWidgets.QPushButton(self.centralwidget)
        self.yf_btn.setGeometry(QtCore.QRect(720, 420, 93, 28))
        self.yf_btn.setObjectName("yf_btn")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(720, 600, 93, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setBold(True)
        font.setWeight(75)
        self.clear_btn.setFont(font)
        self.clear_btn.setObjectName("clear_btn")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(690, 560, 161, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.yy_btn = QtWidgets.QPushButton(self.centralwidget)
        self.yy_btn.setGeometry(QtCore.QRect(720, 490, 93, 28))
        self.yy_btn.setObjectName("yy_btn")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(720, 220, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/wenjian.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menufile.setIcon(icon)
        self.menufile.setObjectName("menufile")
        self.menuclear_DFA = QtWidgets.QMenu(self.menubar)
        self.menuclear_DFA.setObjectName("menuclear_DFA")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open_btn = QtWidgets.QAction(MainWindow)
        self.open_btn.setObjectName("open_btn")
        self.actionread_dfa = QtWidgets.QAction(MainWindow)
        self.actionread_dfa.setObjectName("actionread_dfa")
        self.actionclear = QtWidgets.QAction(MainWindow)
        self.actionclear.setObjectName("actionclear")
        self.menufile.addAction(self.open_btn)
        self.menufile.addAction(self.actionread_dfa)
        self.menuclear_DFA.addAction(self.actionclear)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuclear_DFA.menuAction())

        self.retranslateUi(MainWindow)
        self.cf_btn.clicked.connect(MainWindow.cf_analyze)
        self.lexical_rule_btn.clicked.connect(MainWindow.dfa_trans)
        self.clear_btn.clicked.connect(MainWindow.clear_editor)
        self.grammar_rules_btn.clicked.connect(MainWindow.grammar)
        self.yf_btn.clicked.connect(MainWindow.grammar_analyze)
        self.yy_btn.clicked.connect(MainWindow.semantic_analyze)
        self.pushButton.clicked.connect(MainWindow.semantic)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cf_btn.setText(_translate("MainWindow", "词法分析"))
        self.lexical_rule_btn.setText(_translate("MainWindow", "词法规则"))
        self.grammar_rules_btn.setText(_translate("MainWindow", "语法规则"))
        self.yf_btn.setText(_translate("MainWindow", "语法分析"))
        self.clear_btn.setText(_translate("MainWindow", "clear"))
        self.yy_btn.setText(_translate("MainWindow", "语义分析"))
        self.pushButton.setText(_translate("MainWindow", "语义规则"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuclear_DFA.setTitle(_translate("MainWindow", "clear DFA"))
        self.open_btn.setText(_translate("MainWindow", "open..."))
        self.actionread_dfa.setText(_translate("MainWindow", "read dfa"))
        self.actionclear.setText(_translate("MainWindow", "clear"))
