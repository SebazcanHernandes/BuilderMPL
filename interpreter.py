from lexer import *

def run(code):
    lexer = Lexer(code)
    tokens, error = lexer.create_tokens()
    return tokens, error

while True:
    code = input("BuilderMPL > ")
    result, error = run(code)

    if error:
        print(error.as_string())
    else:
        print(result)
