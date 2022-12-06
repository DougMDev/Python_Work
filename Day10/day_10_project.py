#Calculator
from day_10_art import logo


#Add

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def square(n1, n2):
    return n1 ** n2

Operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for key in Operations:
        print(key)

    should_continue = True

    while should_continue:
        Op_Symbol = input("Pick an Operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = Operations[Op_Symbol]
        answer = calculation_function(num1, num2)
        formed_ans = float("{:.2f".format(answer))

        print(f"{num1} {Op_Symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {formed_ans} or type 'f' to start a new calculation: ") == "y":
            num1 = formed_ans
        else:
            should_continue = False
            calculator()

calculator()
