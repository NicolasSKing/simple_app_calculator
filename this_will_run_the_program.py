from simple_app_calculator_extender import SimpleAppCalculatorExtender

calculator = SimpleAppCalculatorExtender()

try:
    while True:
        print("1 = Addition")
        print("2 = Subtraction")
        print("3 = Multiplication")
        print("4 = Division")
        print("5 = Exit")

        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Thank you for using this program")
            break








