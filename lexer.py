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
    def __init__(self, name, details):
        self.name = name
        self.details = details

    def as_string(self):
        return f"{self.name}: {self.details}"

class FloatingPointError(Error):
    def __init__(self, details):
        super().__init__("Two or more floating points; should only be one.", details)

class UnknownCharacterError(Error):
    def __init__(self, details):
        super().__init__("Illegal character found", details)

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        if self.value:
            return f"{self.type}:{self.value}"
        return f"{self.type}"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def create_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in " \t":
                self.advance()
            elif self.current_char in digits:
                tokens.append(self.make_number())
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
                self.advance()
                return [], UnknownCharacterError("\"" + self.current_char + "\"")
        return tokens, None

    def make_number(self):
        num_str = ""
        dot_count = 0
        while self.current_char != None and self.current_char in digits + ".":
            if self.current_char == ".":
                if dot_count == 1:
                    return [], FloatingPointError("\"" + num_str + "\"")
                    break
                dot_count += 1
                num_str += self.current_char
            else:
                num_str += self.current_char
            self.advance()
        if dot_count == 0:
            return Token(variable_types[0], int(num_str))
        else:
            return Token(variable_types[1], float(num_str))
