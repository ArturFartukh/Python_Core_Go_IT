result = None
operand = None
operator = None
wait_for_number = True

while True:
    result = input()
    if result.isdigit():
        result = int(result)
        break
    else:
        print(f"{result} is not a number. Try again.")

while True:
    while True:
        operator = input()
        if operator in "+-*/=":
            break
        else:
            print(f"{operator} is not '+' or '-' or '/' or '*'. Try again")

    if operator == "=":
        print(f"Result: {result}")
        break

    while True:
        operand = input()
        if operand == "0" and operator == "/":
            print("ZeroDivisionError")
        elif operand.isdigit():
            operand = int(operand)
            break

        else:
            print(f"{operand} is not a number. Try again.")

    if operator == "+":
        result += operand
    elif operator == "-":
        result -= operand
    elif operator == "*":
        result *= operand
    else:
        result /= operand
