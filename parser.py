from functions import *

# Grab code
code = input()
code = code.replace(" ", "")

# Store variables for arithmetic operating
numbers = []
num_source = ""
num_ind = 0
operators = []
op_ind = 0
float_ind = False

# Loops to look for numbers and operators
while True:
    if num_ind == len(code):
        numbers.append(num_source)
        break
    if check_number(code[num_ind]):
        num_source += code[num_ind]
    elif code[num_ind] == "." and float_ind == False:
        num_source += code[num_ind]
        float_ind = True
    elif code[num_ind] == "." and float_ind == True:
        raise FloatingPointError("Multiple floating points")
    else:
        numbers.append(num_source)
        num_source = ""
        float_ind = False
    num_ind += 1
while True:
    if op_ind == len(code):
        break
    if code[op_ind] == "+" or code[op_ind] == "-" or code[op_ind] == "*" or code[op_ind] == "/":
        operators.append(code[op_ind])
    op_ind += 1

# Code is sent to interpreter
run_code = "print("
for i in range(len(numbers)):
    run_code += f"{numbers[i]}"
    if i < len(numbers) - 1:
        run_code += f"{operators[i]}"
run_code += ")"

with open("interpreter.py", "w") as interpreter:
    interpreter.write(run_code)
