import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *

from BasicClass import *
from CodeEditor import QCodeEditor
from analyzer import Ui_MainWindow
from lexical import Lexical
from lexical_dfa import Dfa_TransTable
from grammar_show import Grammar_Show
from grammar_analyze import GrammarAnalyze
from Semantic import Semantic
from SDT import SDTShow


class MyAnalyzer(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.editor = QCodeEditor(self.ui.centralwidget)
        self.ui.editor.setGeometry(QtCore.QRect(10, 20, 661, 751))
        text = '''open a file \nor type something...'''
        self.ui.editor.setPlainText(text)
        self.ui.editor.setObjectName("editor")
        self.ui.open_btn.triggered.connect(self.open_file)
        self.ui.actionread_dfa.triggered.connect(self.read_dfa)
        self.ui.actionclear.triggered.connect(self.clear_dfa)
        self.lexical_window = Lexical()
        self.dfa_window = None
        self.grammer_show = None
        self.grammar_analyzer = GrammarAnalyze()
        self.semantic_analyzer_page = Semantic()
        self.semantic_analyzer = None
        self.SDTShow = None
        self.setWindowTitle("Analyzer")
        self.table = None

    def clear_editor(self):
        self.ui.editor.clear()

    def clear_dfa(self):
        self.table = None

    def read_dfa(self):
        dfa_file = QFileDialog.getOpenFileName(self, 'choose DFA', 'C:\\Users\\', 'Txt files(*.txt)')[0]
        head = ['letter', '_', 'digit', '0', '1-9', 'option', '/', '"', 'bound', '.', 'E', '+', '-', '1-7', 'x', '0-7',
                'a-f', '*', '=', 'other', 'legal']
        table = {}
        file = None
        if not dfa_file: return
        try:
            file = open(dfa_file)
            trans_table, i = file.readlines(), 0
            for line in trans_table:
                line = [int(x) for x in line.split()]
                cur_dict = {}
                for idx in range(len(line)):
                    if line[idx] != -1:
                        cur_dict[head[idx]] = line[idx]
                table[i] = cur_dict
                i += 1
            self.table = table
        except:
            self.ui.editor.clear()
            self.ui.editor.setPlainText("get DFA transform table failed...")
        finally:
            file.close()

    def open_file(self):
        file_name = \
            QFileDialog.getOpenFileName(self, 'choose file',
                                        'C:\\Users\\omnitrix\\PycharmProjects\\CS_Lab1\\test files',
                                        'Txt files(*.txt)')[0]
        file = None
        try:
            file = open(file_name)
            texts = file.read()
            self.ui.editor.clear()
            self.ui.editor.setPlainText(texts)
        except Exception as e:
            self.ui.editor.clear()
            self.ui.editor.setPlainText(str(e))
        finally:
            if file:
                file.close()

    def lexical(self, all_res=True):
        dfa = Cf_Dfa(self.table)
        texts = self.ui.editor.toPlainText().split("\n")
        results = []
        errors = []
        res_lines = []
        info_lines = []
        i = 1
        for line in texts:
            dfa.analyze(line)
            results.extend(dfa.results)
            res_lines.extend([i] * len(dfa.results))
            errors.extend(dfa.error)
            info_lines.extend([i] * len(dfa.error))
            i += 1
        if not all_res:
            return results, res_lines
        return results, errors, res_lines, info_lines

    def cf_analyze(self):
        results, errors, res_lines, info_lines = self.lexical()
        res_num = len(results)
        info_num = len(errors)
        token_table = self.lexical_window.ui.token_table
        info_table = self.lexical_window.ui.infos_table
        token_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        token_table.setRowCount(res_num)
        info_table.setRowCount(info_num)
        for i in range(res_num):
            for j in range(2):
                token_table.setItem(i, j, QTableWidgetItem(str(results[i][j])))
            token_table.setItem(i, 2, QTableWidgetItem(str(res_lines[i])))
        for i in range(info_num):
            for j in range(2):
                info_table.setItem(i, j, QTableWidgetItem(str(errors[i][j])))
            info_table.setItem(i, 2, QTableWidgetItem(str(info_lines[i])))
        self.lexical_window.show()
        return results

    def dfa_trans(self):
        if not self.dfa_window:
            self.dfa_window = Dfa_TransTable()
            trans = Cf_Dfa().move_func
            table = self.dfa_window.ui.trans_table
            table.setRowCount(21)
            for i in range(20):
                for j in range(21):
                    if i in trans:
                        idx = table.horizontalHeaderItem(j).text()
                        if idx in trans[i]:
                            table.setItem(i, j, QTableWidgetItem(str(trans[i][idx])))
        self.dfa_window.show()

    @staticmethod
    def grammar_init(analyzer):
        analyzer = analyzer()
        analyzer.set_grammar()
        analyzer.generate()
        return analyzer

    def grammar(self):
        if not self.grammer_show:
            self.grammer_show = Grammar_Show()
            analyzer = self.grammar_init(GrammarAnalyzer)
            forcast_table = self.grammer_show.ui.Forcast_Table
            forcast_table.setColumnCount(len(analyzer.inputs))
            forcast_table.setRowCount(len(analyzer.Vn))
            forcast_table.setHorizontalHeaderLabels(analyzer.inputs)
            forcast_table.setVerticalHeaderLabels(analyzer.Vn)
            ff_table = self.grammer_show.ui.FF_Table
            select_table = self.grammer_show.ui.Select_Table
            ff_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            select_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            ff_table.setRowCount(len(analyzer.Vn))
            ff_table.setVerticalHeaderLabels(analyzer.Vn)
            for i in range(len(analyzer.Vn)):
                for j in range(len(analyzer.inputs)):
                    symbol = forcast_table.horizontalHeaderItem(j).text()
                    vn = forcast_table.verticalHeaderItem(i).text()
                    if symbol in analyzer.forcast_table[vn]:
                        item = analyzer.forcast_table[vn][symbol]
                        production = str(vn + '->' + item) if item != "synch" else "synch"
                        forcast_table.setItem(i, j, QTableWidgetItem(production))
                vn = ff_table.verticalHeaderItem(i).text()
                ff_table.setItem(i, 0, QTableWidgetItem(str(analyzer.first[vn])))
                ff_table.setItem(i, 1, QTableWidgetItem(str(analyzer.follow[vn])))
            select_table.setRowCount(len(analyzer.select))
            i = 0
            for key in analyzer.select:
                select_table.setItem(i, 0, QTableWidgetItem(key))
                select_table.setItem(i, 1, QTableWidgetItem(str(analyzer.select[key])))
                i += 1
        self.grammer_show.show()

    def grammar_analyze(self):
        analyzer = self.grammar_init(GrammarAnalyzer)
        tokens, lines = self.lexical(False)
        results, errors, props = analyzer.analyze(tokens, lines)
        self.show_grammar(results, errors, props, analyzer)

    def semantic_analyze(self):
        if not self.semantic_analyzer:
            self.semantic_analyzer = self.grammar_init(SemanticAnalyzer)
        else:
            self.semantic_analyzer.semantic_init()
        tokens, lines = self.lexical(False)
        self.semantic_analyzer.analyze(tokens, lines)
        self.show_semantic()

    def show_semantic(self):
        self.semantic_analyzer_page = Semantic()
        info_table = self.semantic_analyzer_page.ui.infos_table
        symbol_table = self.semantic_analyzer_page.ui.symbol_table
        results_table = self.semantic_analyzer_page.ui.result_table
        results_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        results = self.semantic_analyzer.addr_code
        symbols = self.semantic_analyzer.symbol_table
        errors = self.semantic_analyzer.errors
        results_table.setRowCount(len(results))
        symbol_table.setRowCount(len(symbols))
        info_table.setRowCount(len(errors))
        for i in range(len(results)):
            results_table.setItem(i, 0, QTableWidgetItem(str(i)))
            results_table.setItem(i, 1, QTableWidgetItem(results[i]["code"]))
            results_table.setItem(i, 2, QTableWidgetItem(results[i]["quater"]))
        i = 0
        for name in symbols:
            symbol_table.setItem(i, 0, QTableWidgetItem(str(name)))
            symbol_table.setItem(i, 1, QTableWidgetItem(str(symbols[name]['type'])))
            symbol_table.setItem(i, 2, QTableWidgetItem(str(symbols[name]['offset'])))
            i += 1
        i = 0
        for item in errors:
            info_table.setItem(i, 0, QTableWidgetItem(str(item[0])))
            info_table.setItem(i, 1, QTableWidgetItem(str(item[1])))
            info_table.setItem(i, 2, QTableWidgetItem(str(item[2])))
            i += 1
        self.semantic_analyzer_page.show()

    def semantic(self):
        if not self.SDTShow:
            self.SDTShow = SDTShow()
            file = open("./test files/SDT show.txt", "r", encoding="UTF-8")
            lines = file.readlines()
            table = self.SDTShow.ui.SDT_Table
            table.setRowCount(len(lines))
            table.setColumnCount(1)
            table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            for i in range(len(lines)):
                table.setItem(i, 0, QTableWidgetItem(lines[i]))
            file.close()
        self.SDTShow.show()

    def show_grammar(self, results, errors, props, grammar):
        analyzer = self.grammar_analyzer
        tree = analyzer.ui.treeWidget
        tree.clear()
        tree.setColumnCount(1)
        root = QTreeWidgetItem(tree)
        root.setText(0, "Program")
        stack = [root]
        for production in results:
            left, right = production.split('->')
            while left != stack[-1].text(0):
                stack.pop()
            father = stack.pop()
            right = right.split()
            temp = []
            for item in right:
                child = QTreeWidgetItem(father)
                child.setText(0, item)
                if item in grammar.Vn:
                    temp.append(child)
            temp.reverse()
            stack.extend(temp)
        item = QtWidgets.QTreeWidgetItemIterator(tree)
        while item.value():
            node = item.value()
            if node.text(0) == "id" or node.text(0) == "digit":
                leaf = QTreeWidgetItem(item.value())
                leaf.setText(0, props.pop(0))
            item = item.__iadd__(1)
        tree.expandAll()
        table = analyzer.ui.infos_table
        table.clear()
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setVisible(False)
        table.setRowCount(len(errors))
        for i in range(len(errors)):
            for j in range(3):
                table.setItem(i, j, QTableWidgetItem(str(errors[i][j])))
        analyzer.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_analyzer = MyAnalyzer()
    my_analyzer.show()
    sys.exit(app.exec_())
