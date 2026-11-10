def add(a,b):
    print(f"Sum: {a} + {b} = {a+b}")


def sub(a, b):
    print(f"Difference: {a} - {b} = {a-b}")


def mul(a, b):
    print(f"Product: {a} * {b} = {a*b}")


def div(a, b):
    try:
        print(f"Quotient: {a//b}, Remainder: {a%b}")
    except:
        print("Division by 0 is not possible.")