variable_types = [
    "int", "float", "str", "char", "bool", "var", "datetime"
]

operator_types = [
    ["assign", "less", "greater", "less_equal", "greater_equal", "unequal"],
    ["plus", "minus", "multiply", "divide", "modulus", "exponent", "xor"],
    ["increment", "decrement"]
]

symbols = [
    ["left_paren", "right_paren"]
]

special_keywords = [
    ["if", "but if", "but", "when", "do", "for", "switch"]
]

digits = "0123456789"

class Error:
    def __init__(self, pos_start, pos_end, name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.name = name
        self.details = details

    def as_string(self):
        error_result = f"{self.name}: {self.details}\nFile {self.pos_start.filename}, line {self.pos_start.line + 1}"
        return error_result

class FloatingPointError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'FloatingPointError', details)

class UnknownCharacterError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'UnknownCharacterError', details)

class Position:
    def __init__(self, index, line, column, filename, filetext):
        self.index = index
        self.line = line
        self.column = column
        self.filename = filename
        self.filetext = filetext

    def advance(self, current_char):
        self.index += 1
        self.column += 1
        if current_char == "\n":
            self.line += 1
            self.col = 0
        return self

    def copy(self):
        return Position(self.index, self.line, self.column, self.filename, self.filetext)

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        if self.value:
            return f"{self.type}:{self.value}"
        return f"{self.type}"

class Lexer:
    def __init__(self, filename, text):
        self.filename = filename
        self.text = text
        self.pos = Position(-1, 0, -1, self.filename, self.text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.index] if self.pos.index < len(self.text) else None

    def create_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in " \t":
                self.advance()
            elif self.current_char in digits:
                token = self.make_number()
                if token == None:
                    pos_start = self.pos.copy()
                    self.advance()
                    return [], FloatingPointError(pos_start, self.pos, "Two or more floating points in a variable\n\t" + self.text)
                tokens.append(token)
            elif self.current_char == "+":
                tokens.append(operator_types[1][0])
                self.advance()
            elif self.current_char == "-":
                tokens.append(operator_types[1][1])
                self.advance()
            elif self.current_char == "*":
                tokens.append(operator_types[1][2])
                self.advance()
            elif self.current_char == "/":
                tokens.append(operator_types[1][3])
                self.advance()
            elif self.current_char == "%":
                tokens.append(operator_types[1][4])
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], UnknownCharacterError(pos_start, self.pos, "Unsupported character found\n\t\"" + char + "\"")
        return tokens, None

    def make_number(self):
        num_str = ""
        dot_count = 0
        while self.current_char != None and self.current_char in digits + ".":
            if self.current_char == ".":
                if dot_count == 1:
                    return None
                dot_count += 1
                num_str += self.current_char
            else:
                num_str += self.current_char
            self.advance()
        if dot_count == 0:
            return Token(variable_types[0], int(num_str))
        else:
            return Token(variable_types[1], float(num_str))
