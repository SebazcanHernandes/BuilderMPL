from functions import *
import io

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
func_check = False

# Interpreted code goes here
run_code = ""

# Look for functions
while not check_number(code[num_ind]):
    if code[num_ind] + code[num_ind + 1] + code[num_ind + 2] + code[num_ind + 3] == "say(":
        run_code += "print("
        func_check = True
    num_ind += 1

# Loops to look for numbers and operators
if check_number(code[num_ind]):
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
        elif code[num_ind] == ")" and func_check == True:
            num_ind += 1
            continue
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
print(numbers, operators)
for i in range(len(numbers)):
    run_code += f"{numbers[i]}"
    if i < len(numbers) - 1:
        run_code += f"{operators[i]}"
if func_check == True:
    run_code += ")"
    func_check = False

with open("interpreter.py", "w") as interpreter:
    interpreter.write(run_code)
