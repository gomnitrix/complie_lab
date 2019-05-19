class Cf_Dfa:
    def __init__(self, move_func=None):
        self.move_func = {  # 状态转移函数
            0: {"letter": 15, "_": 15, "1-9": 1, '0': 7, '/': 11, "option": 16, "\"": 18, "\'": 18, "bound": 20},
            1: {'digit': 1, '.': 2, 'E': 4},
            2: {'digit': 3},
            3: {'digit': 3, 'E': 4},
            4: {'+': 5, '-': 5, 'digit': 6},
            5: {'digit': 6},
            6: {'digit': 6},
            7: {'1-7': 8, 'x': 9},
            8: {'0-7': 8},
            9: {'1-9': 10, 'a-f': 10},
            10: {'digit': 10, 'a-f': 10},
            11: {'*': 12, '=': 17},
            12: {'other': 12, '*': 13},
            13: {'*': 13, 'other': 12, '/': 14},
            15: {"letter": 15, "digit": 15},
            16: {"legal": 17},
            18: {"other": 19},
            19: {"\"": 21, "\'": 21}
        } if not move_func else move_func
        self.current = 0  # 当前状态
        self.results = []  # 目前为止已分析出的结果
        self.error = []  # 错误列表
        self.recent_res = ""  # 最近识别出的结果
        self.recent_fstate = None  # 最近到达的终态
        self.buffer = ""  # 缓存，存放当前已处理还未保存的串
        self.fstates = {1: "10进制整数", 3: "10进制浮点数", 6: "科学记数法", 7: "10进制0", 8: "8进制数", 10: "16进制数", 11: "OP", 14: "NOTE",
                        15: "IDN", 16: "OP", 17: "OP", 21: "CHAR", 20: "BOUND"}  # 终态集合

    def pre_input(self, x):
        x = str(x)
        if self.current == 0:
            if '1' <= x <= '9':
                return "1-9"
            elif x == '0':
                return '0'
            elif x in ['+', '-', '*', '=', '!', '|', '&', '^', '>', '<', '%']:
                return "option"
            elif x in ['{', '[', '(', ')', ']', '}', ',', ';', ':', '?']:
                return "bound"
        elif self.current == 7:
            if '1' <= x <= '7':
                return '1-7'
        elif self.current == 8:
            if '0' <= x <= '7':
                return '0-7'
        elif self.current == 9 or self.current == 10:
            if x.isdigit():
                if self.current == 9 and x != '0':
                    return '1-9'
                elif self.current == 10:
                    return "digit"
            elif 'a' <= x <= 'f':
                return 'a-f'
        elif (self.current == 12 or self.current == 13) and x != "*":
            return "other"
        elif self.current == 16:
            if self.buffer + x in ["+=", "-=", "*=", "++", "--", "!=", "==", ">=", "<=", ">>", "<<", "&&", "||"]:
                return "legal"
            else:
                self.error_analyze(self.buffer, x)
        elif self.current == 18 and x != "\"" and x != "\'":
            return "other"
        if self.is_letter(x):
            return "letter"
        elif x.isdigit():
            return 'digit'
        return None

    @staticmethod
    def is_letter(x):
        return 'A' <= x <= 'Z' or 'a' <= x <= 'z'

    def move(self, x):
        mv_func = self.move_func[self.current]
        cat = self.pre_input(x)
        if x in mv_func:
            self.current = mv_func[x]
        elif cat in mv_func:
            self.current = mv_func[cat]
        else:
            raise Exception
        self.buffer += x
        if self.current in self.fstates:
            self.recent_res = self.buffer
            self.recent_fstate = self.current

    def dfa_init(self):
        self.current = 0
        self.buffer = ""
        self.recent_res = ""
        self.recent_fstate = None

    def ID_classify(self):
        if self.recent_res in ["while", "int", "double", "float", "if", "else", "const", "for", "break", "continue",
                               "do", "case", "switch", "return", "default", "long", "short", "char", "signed",
                               "unsigned", "auto", "struct", "union", "enum", "typedef", "record", "proc", "call",
                               "then", "and", "or", "real", 'not', "true", "false"]:
            up = self.recent_res.upper()
            return self.recent_res, "<{},_>".format(up)
        else:
            return self.recent_res, "<IDN,{}>".format(self.recent_res)

    def classify(self):
        clss = ""
        if self.recent_fstate in self.fstates:
            clss = self.fstates[self.recent_fstate]
        res = (self.recent_res, "<{},{}>".format(clss, self.recent_res))
        try:
            if clss == "BOUND":
                res = (self.recent_res, "<BOUND,{}>".format(self.recent_res))
            elif clss == "IDN":
                res = self.ID_classify()
            elif clss == "NOTE":
                res = ('/**/', '<NOTE,_>')
        except Exception as e:
            self.error.append((self.recent_res, str(e)))
        self.results.append(res)
        self.dfa_init()

    def error_handing(self, idx):
        buffer = ""
        if self.buffer:
            buffer = self.buffer
        self.dfa_init()
        if buffer:
            self.buffer = buffer
        return idx + 1

    def error_analyze(self, buffer=None, ch=None):
        current = self.current
        if not buffer: buffer = self.buffer
        buffer += ch
        if (current == 7 or current == 8) and (self.is_letter(ch) or '9' >= ch > '7'):
            self.error.append((buffer, "错误的8进制"))
        elif (current == 9 or current == 10) and ('f' < ch <= 'z' or 'F' < ch <= 'Z'):
            self.error.append((buffer, "错误的16进制"))
        elif (current == 9) and (ch == '0'):
            self.error.append((buffer, "错误的16进制"))
        elif (current == 2 or current == 3) and (self.is_letter(ch)):
            self.error.append((buffer, "错误的浮点数"))
        elif (current == 4 or current == 5 or current == 6) and self.is_letter(ch):
            self.error.append((buffer, "错误的科学记数法"))
        elif current == 16 and ch in ['+', '-', '*', '=', '!', '|', '&', '^', '>', '<', '%']:
            self.error.append((buffer, "错误的计算符"))
        elif current == 19:
            self.error.append((buffer, "错误的字符常量"))
            self.buffer = ""

    def analyze(self, code):
        lth = len(code)
        i = 0
        self.error = []
        self.results = []
        while i < lth:
            ch = code[i]
            try:
                self.move(ch)
                i += 1
            except:
                buffer = self.buffer
                if self.recent_fstate:
                    if not ch.isspace():
                        self.error_analyze(buffer, ch)
                    back_num = len(buffer) - len(self.recent_res)
                    self.classify()
                    i -= back_num
                    continue
                else:
                    self.error_analyze(buffer, ch)
                    i = self.error_handing(i)
                    if code[i - 1] != ' ' and code[i - 1] != '\t':
                        self.error.append((code[i - 1], "illegal input"))
            if i == lth and self.recent_fstate:
                self.classify()
            elif i == lth:
                self.error_handing(i)


def check_grammar(func):
    def safely_set(self, start="Program"):
        if not self.grammar:
            raise Exception("grammar is null")
        func(self, start)

    return safely_set


class GrammarAnalyzer:
    def __init__(self):
        self.grammar = {}
        self.Vt = set()
        self.Vn = set()
        self.first = {}
        self.follow = {}
        self.select = {}
        self.forcast_table = {}
        self.inputs = ['$', 'proc', 'int', 'real', 'char', 'record', 'id', 'if', 'while', 'call', 'return', 'switch',
                       'for', '}', '=', ';', ',', ')', '[', '++', '--', 'case', 'default', '(', 'digit', '+', '<', '<=',
                       '==', '!=', '>', '>=', 'and', 'or', 'then', 'do', '*', 'not', 'true', 'false']

    def set_grammar(self, path="./test files/grammar.txt"):
        file = None
        tem = []
        try:
            file = open(path, 'r')
            grammars = file.readlines()
            if grammars:
                for grammar in grammars:
                    if grammar.isspace():
                        continue
                    grammar = grammar.strip()
                    t, g = grammar.split('->')
                    g = g.split('|')
                    t = t.strip()
                    self.Vn.add(t)
                    if not self.grammar.get(t):
                        self.grammar[t] = []
                    self.grammar[t].extend(g)
                    tem.append(g)
                for g in tem:
                    for item in g:
                        symbols = item.split()
                        for i in symbols:
                            if (i.islower() or not i.isalpha()) and not (i in self.Vn):
                                self.Vt.add(i)
        except FileNotFoundError:
            print("no such File")
        finally:
            file.close()

    @check_grammar
    def generate(self, start="Program"):
        symbols = self.Vn
        for symbol in symbols:
            self.set_first(symbol)
        while True:
            flag = 0
            for symbol in symbols:
                result = self.set_follow(symbol, start)
                if result:
                    flag = 1
            if not flag:
                break
        self.set_select()
        self.set_forcast_table()

    def get_production_first(self, production):
        symbols = production.split()
        first, length, i = set(), len(symbols), 0
        for symbol in symbols:
            if symbol in self.Vt:
                first.add(symbol)
                break
            if not self.first.get(symbol):
                self.set_first(symbol)
            if i == len(symbols) - 1:
                first |= self.first.get(symbol)
            else:
                first |= (self.first.get(symbol) - {'empty'})
                if 'empty' not in self.first.get(symbol):
                    break
            i += 1
        return first

    def set_first(self, symbol):
        if self.first.get(symbol):
            return
        first = set()
        if symbol in self.Vt:
            first.add(symbol)
        elif symbol in self.Vn:
            productions = self.grammar[symbol]
            for production in productions:
                first |= self.get_production_first(production)
        self.first[symbol] = first

    def set_follow(self, symbol, start):
        follow = set()
        if symbol == start:
            follow.add('$')
        for key in self.grammar:
            for production in self.grammar[key]:
                splt = production.split()
                if symbol in splt:
                    idx = splt.index(symbol)
                    last = ' '.join(splt[idx + 1:])
                    first, flag = [], 0
                    if last or flag:
                        first = self.get_production_first(last)
                        follow |= (first - {'empty'})
                    if (key != symbol and (not last or ('empty' in first))) or (
                            symbol == 'E' and production == "E Relop E"):
                        if self.follow.get(key):
                            follow |= self.follow.get(key)
        old_follow = self.follow.get(symbol)
        flag, new_length, old_length = 0, len(follow), len(old_follow) if old_follow else 0
        if new_length > old_length:
            flag = 1
        self.follow[symbol] = follow
        return flag

    def set_select(self):
        for key in self.grammar:
            for production in self.grammar[key]:
                first = self.get_production_first(production)
                if 'empty' not in first:
                    self.select[key + '->' + production] = first
                else:
                    self.select[key + '->' + production] = (first - {'empty'}) | self.follow.get(key)

    def set_forcast_table(self):
        for v in self.Vn:
            self.forcast_table[v] = {}
            for production in self.grammar[v]:
                for item in self.select[v + '->' + production]:
                    self.forcast_table[v][item] = production
            for item in self.follow[v]:
                if item not in self.forcast_table[v]:
                    self.forcast_table[v][item] = "synch"
        self.forcast_table['H\'']['and'] = 'and I H\''
        self.forcast_table['I']['('] = '( B )'

    @staticmethod
    def pretreatment(token):
        current = token[1].split(',')[0][1:].lower()
        if current == 'idn':
            return 'id'
        elif current in ["10进制整数", "10进制浮点数", "科学记数法", "10进制0", "8进制数", "16进制数"]:
            return 'digit'
        elif current == 'op' or current == 'bound':
            return token[0]
        else:
            return current

    def analyze(self, tokens, lines):
        stack = ['$', 'Program']
        i = 0
        length = len(tokens)
        results, errors, props = [], [], []
        while stack:
            token = None
            if i < length:
                current = self.pretreatment(tokens[i])
                token = tokens[i]
                if current == 'note':
                    i += 1
                    continue
            else:
                current = '$'
            top = stack[-1]
            while top == 'empty':
                stack.pop()
                top = stack[-1]
            if current == top and top == '$':
                break
            elif current == top:
                stack.pop()
                i += 1
                if (current == "id" or current == "digit") and token:
                    props.append(token[0])
                continue
            elif top not in self.Vn:
                pop = stack.pop()
                line = lines[i] if i < length else lines[-1]
                errors.append((current, "缺少" + pop, line))
            elif current in self.forcast_table[top]:
                stack.pop()
                production = self.forcast_table[top][current].split()
                if production == ["synch"]:
                    continue
                production.reverse()
                stack.extend(production)
                results.append(top + '->' + self.forcast_table[top][current])
            elif current == '$':
                stack.pop()
                continue
            else:
                if (current == "id" or current == "digit") and token:
                    errors.append((token[0], "多余字符：" + token[0], lines[i]))
                elif token:
                    errors.append((current, "多余字符：" + current, lines[i]))
                i += 1
        if i < length:
            errors.append(("", "tokens未分析完", ""))
        return results, errors, props


from collections import defaultdict


class SemanticAnalyzer:
    def __init__(self):
        self.grammar = {}
        self.Vt = set()
        self.Vn = set()
        self.first = {}
        self.follow = {}
        self.select = {}
        self.forcast_table = {}
        self.temp = defaultdict(dict)
        self.SDT = {}
        self.symbol_table = defaultdict(dict)
        self.errors = []
        self.addr_code = defaultdict(dict)
        self.idx = 0
        self.nextquad = 0
        self.queen = []
        self.offset, self.t, self.w = 0, None, None
        self.inputs = ['$', 'proc', 'int', 'real', 'char', 'record', 'id', 'if', 'while', 'call', 'return', 'switch',
                       'for', '}', '=', ';', ',', ')', '[', '++', '--', 'case', 'default', '(', 'digit', '+', '<', '<=',
                       '==', '!=', '>', '>=', 'and', 'or', 'then', 'do', '*', 'not', 'true', 'false']
        self.backup = []

    def semantic_init(self):
        self.temp = defaultdict(dict)
        self.symbol_table = defaultdict(dict)
        self.errors = []
        self.addr_code = defaultdict(dict)
        self.idx = 0
        self.nextquad = 0
        self.queen = []
        self.offset, self.t, self.w = 0, None, None

    def set_grammar(self, path="./test files/semantic_grammar.txt"):
        file, file2 = None, None
        tem = []
        try:
            file = open(path, 'r')
            grammars = file.readlines()
            if grammars:
                for grammar in grammars:
                    if grammar.isspace():
                        continue
                    grammar = grammar.strip()
                    t, g = grammar.split('->')
                    g = g.split('|')
                    t = t.strip()
                    self.Vn.add(t)
                    if not self.grammar.get(t):
                        self.grammar[t] = []
                    self.grammar[t].extend(g)
                    tem.append(g)
                for g in tem:
                    for item in g:
                        symbols = item.split()
                        for i in symbols:
                            if (i.islower() or not i.isalpha()) and not (i in self.Vn):
                                self.Vt.add(i)
            file2 = open("./test files/SDT.txt", 'r', encoding="UTF-8")
            sdts = file2.readlines()
            for sdt in sdts:
                grammar, sdt = sdt.split('?')
                self.SDT[grammar] = sdt
        except FileNotFoundError:
            print("no such File")
        finally:
            file.close()
            file2.close()

    @check_grammar
    def generate(self, start="Program"):
        symbols = self.Vn
        for symbol in symbols:
            self.set_first(symbol)
        while True:
            flag = 0
            for symbol in symbols:
                result = self.set_follow(symbol, start)
                if result:
                    flag = 1
            if not flag:
                break
        self.set_select()
        self.set_forcast_table()

    def get_production_first(self, production):
        symbols = production.split()
        first, length, i = set(), len(symbols), 0
        for symbol in symbols:
            if symbol in self.Vt:
                first.add(symbol)
                break
            if not self.first.get(symbol):
                self.set_first(symbol)
            if i == len(symbols) - 1:
                first |= self.first.get(symbol)
            else:
                first |= (self.first.get(symbol) - {'empty'})
                if 'empty' not in self.first.get(symbol):
                    break
            i += 1
        return first

    def set_first(self, symbol):
        if self.first.get(symbol):
            return
        first = set()
        if symbol in self.Vt:
            first.add(symbol)
        elif symbol in self.Vn:
            productions = self.grammar[symbol]
            for production in productions:
                first |= self.get_production_first(production)
        self.first[symbol] = first

    def set_follow(self, symbol, start):
        follow = set()
        if symbol == start:
            follow.add('$')
        for key in self.grammar:
            for production in self.grammar[key]:
                splt = production.split()
                if symbol in splt:
                    idx = splt.index(symbol)
                    last = ' '.join(splt[idx + 1:])
                    first, flag = [], 0
                    if last or flag:
                        first = self.get_production_first(last)
                        follow |= (first - {'empty'})
                    if (key != symbol and (not last or ('empty' in first))) or (
                            symbol == 'E' and production == "E Relop E"):
                        if self.follow.get(key):
                            follow |= self.follow.get(key)
        old_follow = self.follow.get(symbol)
        flag, new_length, old_length = 0, len(follow), len(old_follow) if old_follow else 0
        if new_length > old_length:
            flag = 1
        self.follow[symbol] = follow
        return flag

    def set_select(self):
        for key in self.grammar:
            for production in self.grammar[key]:
                first = self.get_production_first(production)
                if 'empty' not in first:
                    self.select[key + '->' + production] = first
                else:
                    self.select[key + '->' + production] = (first - {'empty'}) | self.follow.get(key)

    def set_forcast_table(self):
        for v in self.Vn:
            self.forcast_table[v] = {}
            for production in self.grammar[v]:
                for item in self.select[v + '->' + production]:
                    self.forcast_table[v][item] = production
            for item in self.follow[v]:
                if item not in self.forcast_table[v]:
                    self.forcast_table[v][item] = "synch"
        self.forcast_table['I']['('] = '( I )'

    @staticmethod
    def pretreatment(token):
        current = token[1].split(',')[0][1:].lower()
        if current == 'idn':
            return 'id'
        elif current in ["10进制整数", "10进制浮点数", "科学记数法", "10进制0", "8进制数", "16进制数"]:
            return 'digit'
        elif current == 'op' or current == 'bound':
            return token[0]
        else:
            return current

    def enter(self, line, name, stype, offset):
        if name in self.symbol_table:
            self.errors.append((name, "重复声明", line))
        self.symbol_table[name]['type'] = stype
        self.symbol_table[name]['offset'] = offset

    def lookup(self, addr, line):
        if addr not in self.symbol_table:
            self.errors.append((addr, "变量未经声明", line))

    def newtemp(self):
        self.idx += 1
        return 't' + str(self.idx - 1)

    def gen(self, code):
        if "*empty" in code:
            self.temp['G']['addr'] = self.temp['F']['addr']
            self.idx -= 1
        elif "+empty" in code:
            self.temp['E']['addr'] = self.temp['G']['addr']
            self.idx -= 1
        else:
            self.addr_code[self.nextquad]["code"] = code
            self.nextquad += 1

    def makelist(self, nextquad):
        return [nextquad]

    def backpatch(self, alist, quad):
        for command in alist:
            self.addr_code[command]["code"] = self.addr_code[command]["code"].format(str(quad))
            self.addr_code[command]["quater"] = self.addr_code[command]["quater"].format(str(quad))

    def merge(self, list1, list2):
        new = []
        new.extend(list1)
        new.extend(list2)
        return new

    def quaternary(self, op, p1, p2, key):
        if p2 == "empty":
            return
        self.addr_code[self.nextquad - 1]["quater"] = "({},{},{},{})".format(op, p1, p2, key)

    def codepoint1(self, value):
        if value:
            self.backup.append(value)

    def codepoint2(self):
        if self.backup:
            self.temp['G']['addr'] = self.backup.pop()

    def codepoint3(self):
        if self.backup:
            self.temp['F']['addr'] = self.backup.pop()

    def codepoint4(self):
        if self.backup:
            self.temp['digit']['lex'] = self.backup.pop()

    def codepoint5(self):
        self.queen = [self.temp['E']['addr']]

    def codepoint6(self):
        self.queen.append(self.temp['E']['addr'])

    def codepoint7(self):
        for item in self.queen:
            self.gen("param " + item)
            self.quaternary("param", "_", "_", item)

    def codepoint8(self):
        if self.backup:
            self.temp['id']['lexeme'] = self.backup.pop()

    def codepoint9(self):
        self.temp["digit"]["index"] = self.temp["digit"]["lex"]

    def codepoint10(self):
        if self.temp['digit']['index']:
            self.temp['L']['addr'] = self.temp['L']['addr'] + "[" + self.temp['digit']['index'] + "]"
            self.temp['digit']['index'] = None

    def codepoint11(self, line):
        if self.temp['id']['lexeme'] in self.symbol_table and self.symbol_table[self.temp['id']['lexeme']]["type"] != "proc":
            self.errors.append((self.temp['id']['lexeme'], "非函数变量", line))

    def codepoint12(self, addr):
        self.temp["id"]["flag"] = addr

    def codepoint13(self, line):
        if self.temp["id"]["flag"] and "array" not in self.symbol_table[self.temp["id"]["flag"]]["type"]:
            self.errors.append((self.temp["id"]["flag"], "非数组变量", line))
            self.temp["id"]["flag"] = None

    def codepoint14(self, line):
        if self.symbol_table[self.temp['id']['lexeme']]["type"] == "real" and "." not in self.temp['F']['addr']:
            self.errors.append((self.temp['F']['addr'], "类型不匹配", line))
            self.temp['F']['addr'] = str(float(self.temp['F']['addr']))
        elif self.symbol_table[self.temp['id']['lexeme']]["type"] == "int" and "." in self.temp['F']['addr']:
            self.errors.append((self.temp['F']['addr'], "类型不匹配", line))
            self.temp['F']['addr'] = str(int(self.temp['F']['addr']))

    def codepoint15(self, line=None):
        if not self.temp['X'].get("flag"):
            self.temp['X']['flag'] = self.temp['X']['type']
        else:
            if self.temp['E']['addr'] in self.symbol_table and self.symbol_table[self.temp['E']['addr']]['type'] != self.temp['X']['flag']:
                self.errors.append((self.temp['E']['addr'], "函数返回类型不正确", line))
            self.temp['X']['flag'] = None

    def array(self, num, t):
        return "array({},{})".format(num, t)

    def analyze(self, tokens, lines):
        stack = ['$', 'Program']
        i = 0
        length = len(tokens)
        while stack:
            token = None
            if i < length:
                current = self.pretreatment(tokens[i])
                token = tokens[i]
                if current == 'note':
                    i += 1
                    continue
            else:
                current = '$'
            top = stack[-1]
            while top == 'empty':
                stack.pop()
                top = stack[-1]
            if current == top and top == '$':
                break
            elif current == top:
                stack.pop()
                i += 1
                if token and (current == "id" or current == "digit" or (current == "char" and token[0] != "char")):
                    if current == "id":
                        self.temp['id']['lexeme'] = token[0]
                    elif current == "digit":
                        self.temp['digit']['lex'] = token[0]
                    else:
                        self.temp['char']['lex'] = token[0]
                if current in [">", "<", ">=", "<=", "==", "!="]:
                    self.temp['Relop']['val'] = current
                continue
            elif '{' in top:
                codes = top.strip('{}').split(';')
                for code in codes:
                    if code and not code.isspace():
                        try:
                            exec(code)
                        except KeyError as e:
                            print(code)
                        except Exception as e:
                            print(code)
                            raise e
                stack.pop()
            elif top not in self.Vn:
                pop = stack.pop()
                if pop == "digit":
                    i += 1
                    self.errors.append((token[0], "非法下标", lines[i]))
            elif current in self.forcast_table[top]:
                stack.pop()
                production = self.forcast_table[top][current]
                if production == "synch":
                    continue
                sdt = self.SDT[top + '->' + production]
                sdt = sdt.split()
                sdt.reverse()
                stack.extend(sdt)
            elif current == '$':
                stack.pop()
                continue
            else:
                i += 1
        self.addr_code[self.nextquad]["code"] = "exit"
        self.addr_code[self.nextquad]["quater"] = "(exit,_,_,0)"


if __name__ == '__main__':
    test = SemanticAnalyzer()
    # test.set_grammar("./test files/test.txt")
    # test.generate(start="E")
    test.set_grammar()
    test.generate()
    print(test.first)
    print(test.follow)
