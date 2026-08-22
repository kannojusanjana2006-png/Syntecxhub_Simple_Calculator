def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b


def calculator():
    while True:
        print("\n--- SIMPLE CALCULATOR ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Clear")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "6":
            print("Calculator closed. Thank you!")
            break

        elif choice == "5":
            print("Calculator cleared!")

        elif choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = add(num1, num2)

                elif choice == "2":
                    result = subtract(num1, num2)

                elif choice == "3":
                    result = multiply(num1, num2)

                elif choice == "4":
                    result = divide(num1, num2)

                print("Result =", result)

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        else:
            print("Invalid choice! Please select from 1 to 6.")


calculator()
