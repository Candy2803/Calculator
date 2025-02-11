def calculator():
    num1 = input("Enter First number: ")
    num1 = int(num1)
    num2 = input("Enter Second number: ")
    num2 = int(num2)
    operation = input("Enter Operation: ")

    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        if num2 > 0:
            print(num1 / num2)
        else:
            print("Cannot divide by 0")
    else:
        print("Syntax Error")
        
calculator()