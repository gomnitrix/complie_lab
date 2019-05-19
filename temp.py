class Cf_Dfa:
    def __init__(self):
        self.states = []
        self.move_func = {
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
            18: {"other": 18, "\"": 19, "\'": 19},
        }
        self.current = 0
        self.results = []
        self.error = []
        self.recent_res = ""
        self.recent_fstate = None
        self.buffer = ""
        self.half_close = []
        self.fstates = {1: "10进制整数", 3: "10进制浮点数", 6: "科学记数法", 7: "10进制0", 8: "8进制数", 10: "16进制数", 14: "注释",
                        15: "标识符", 16: "运算符", 17: "运算符", 19: "字符串常量", 20: "界符"}

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
        elif self.current == 12 and x != "*":
            return "other"
        elif self.current == 16:
            if self.buffer + x in ["+=", "-=", "*=", "++", "--", "!=", "==", ">=", "<=", ">>", "<<", "&&", "||"]:
                return "legal"
        elif self.current == 18 and x != "\"" and x != "\'":
            return "other"
        if 'A' <= x <= 'Z' or 'a' <= x <= 'z':
            return "letter"
        elif x.isdigit():
            return 'digit'
        return None

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
        self.error = []

    def bound_classify(self):
        if self.recent_res in ['{', '[', '(']:
            self.half_close.append(self.recent_res)
            self.dfa_init()
            return True
        elif self.recent_res in [')', ']', '}']:
            if self.half_close:
                flag = chr(ord(self.recent_res) - 1) == self.half_close[-1] or chr(ord(self.recent_res) - 2) == \
                       self.half_close[-1]
                if flag:
                    half = self.half_close.pop()
                    self.results.append((half, "<{},_>".format(half)))
                else:
                    raise Exception("界符不匹配")
            else:
                raise Exception("错误的界符")
            return False

    def ID_classify(self):
        if self.recent_res in ["while", "int", "double", "float", "if", "else", "const", "for", "break", "continue",
                               "do", "case", "switch", "return", "default", "long", "short", "char", "signed",
                               "unsigned"]:
            up = self.recent_res.upper()
            return (self.recent_res, "<{},_>".format(up))
        else:
            return (self.recent_res, "<IDN,{}>".format(self.recent_res))

    def classify(self):
        clss = ""
        if self.recent_fstate in self.fstates:
            clss = self.fstates[self.recent_fstate]
        res = (self.recent_res, "<{},{}>".format(clss, self.recent_res))
        try:
            if clss == "界符":
                res = (self.recent_res, "<{},_>".format(self.recent_res))
                if self.bound_classify():
                    return
            elif clss == "标识符":
                res = self.ID_classify()
            elif clss == "注释":
                res = ('/**/', '<NOTE,_>')
        except Exception as e:
            self.error.append((self.recent_res, str(e)))
        self.results.append(res)
        self.dfa_init()

    def error_handing(self, idx, Mode="Panic"):
        buffer = ""
        if self.buffer:
            buffer = self.buffer
        if Mode == "Panic":
            self.dfa_init()
            if buffer:
                self.buffer = buffer
            return idx + 1
        elif Mode == "EndLine":
            if self.half_close:
                while self.half_close:
                    last = self.half_close.pop()
                    buffer = last + buffer
                self.error.append((buffer, "界符未关闭"))
            elif buffer:
                self.error.append((buffer, "未封闭"))

    def analyze(self, code):
        lth = len(code)
        i = 0
        while i < lth:
            ch = code[i]
            try:
                self.move(ch)
                i += 1
            except:
                buffer = self.buffer
                if self.recent_fstate:
                    back_num = len(buffer) - len(self.recent_res)
                    self.classify()
                    i -= back_num
                    continue
                else:
                    i = self.error_handing(i)
                    if code[i - 1] != ' ' and code[i - 1] != '\t':
                        self.error.append((code[i - 1], "illegal input"))
            if i == lth and self.recent_fstate:
                if self.half_close:
                    self.error_handing(i, Mode="EndLine")
                self.classify()
            elif i == lth:
                self.error_handing(i, Mode="EndLine")
