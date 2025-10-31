
Num1 = int(input("Please enter your first number : "))
Num2 = int(input("Please enter your second number : "))

Operators = input("Please enter operator(+ , - ,* , / , ^) : ")

match Operators:
    case '+':
        result = Num1 + Num2
    case '-':
        result = Num1 - Num2
    case '*':
        result = Num1 * Num2
    case '/':
        if Num2 != 0:
            result = Num1 / Num2
        else:
            result = "Division by zero is not possible!"
    case '^':
        result = Num1 ** Num2
    case _:
        result = "Invalid!"

print(f"Result ({Num1} {Operators} {Num2}):", result)