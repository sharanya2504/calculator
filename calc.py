def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def modulo(x, y):
    return x % y

def floor_division(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x // y

def power(x, y):
    return x ** y

# Main program
while True:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'modulo' for modulo")
    print("Enter 'floor' for floor division")
    print("Enter 'power' for power")
    print("Enter 'quit' to end the program")

    user_input = input("Enter: ")

    if user_input == "quit":
        break
    elif user_input in ('add', 'subtract', 'multiply', 'divide','modulo','floor','power'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            result = add(num1, num2)
            print("The result is", result)
        elif user_input == "subtract":
            result = subtract(num1, num2)
            print("The result is", result)
        elif user_input == "multiply":
            result = multiply(num1, num2)
            print("The result is", result)
        elif user_input == "divide":
            result = divide(num1, num2)
            print("The result is", result)
        elif user_input == "modulo":
            result = modulo(num1, num2)
            print("The result is", result)
        elif user_input == "floor":
            result = floor_division(num1, num2)
            print("The result is", result)
        elif user_input == "power":
            result = power(num1, num2)
            print("The result is", result)
    else:
        print("Unknown input")
