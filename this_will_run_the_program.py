from simple_app_calculator_extender import SimpleAppCalculatorExtender

calculator = SimpleAppCalculatorExtender()

try:
    while True:
        print("1 = Addition")
        print("2 = Subtraction")
        print("3 = Multiplication")
        print("4 = Division")

        choice = int(input("Enter your choice: "))
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))

        if choice == 1:
          calculator.addition(first_number, second_number)
        elif choice == 2:
          calculator.subtract(first_number, second_number)
        elif choice == 3:
          calculator.multiplication(first_number, second_number)
        elif choice == 4:
          calculator.divition(first_number, second_number)
        else:
            print("Please enter a valid choice")
            continue

        again = input("Do you want to continue? (yes/no): ").lower()

        if again != "yes":
            print("Thank you for using this program")
            break

except ValueError:
    print("Invalid input. Please enter a number only")

except ZeroDivisionError:
    print("Cannot divide by zero.")






