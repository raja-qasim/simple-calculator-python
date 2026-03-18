class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = result + a
        return result

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"

        result = 0
        while a >= b:
            a = a - b
            result += 1
        return result

    def modulo(self, a, b):
        if b == 0:
            return "Error: Division by zero"

        while a >= b:
            a = a - b
        return a


# Main Program
if __name__ == "__main__":
    calc = Calculator()

    while True:
        print("\n===== Simple Calculator =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulo")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 6:
            print("Exiting calculator... ")
            break

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == 1:
            print("Result:", calc.add(a, b))

        elif choice == 2:
            print("Result:", calc.subtract(a, b))

        elif choice == 3:
            print("Result:", calc.multiply(a, b))

        elif choice == 4:
            print("Result:", calc.divide(a, b))

        elif choice == 5:
            print("Result:", calc.modulo(a, b))

        else:
            print("Invalid choice! Please try again.")