#Creating the Dashboard Menu
def menu():
    a = float(input("Enter first number: "))
    b = float(input("Enter the second number:" ""))
    print("""
Choose an operation from the list:
1. Addition
2. Subtraction
3. Multiplication
4. Division with remainder
    """)
    op = int(input("Enter your choice: "))
    return a, b, op