# Simple calculator using functions and loop

# Define functions for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return " Can't divide by zero!"
    return a / b

# Main calculator function
def calculator():
    print("Welcome to Command-Line Calculator 👋")
    
    while True:
        # Show options to user
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting... Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print(" Invalid choice. Try again.")
            continue

        # Take two numbers from user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print(" Please enter valid numbers.")
            continue

        # Perform the selected operation
        if choice == '1':
            print(f" Result: {add(num1, num2)}")
        elif choice == '2':
            print(f" Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f" Result: {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f" Result: {result}")

# Run the calculator
calculator()
