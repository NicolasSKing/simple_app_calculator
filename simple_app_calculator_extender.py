from simple_app_calculator import SimpleAppCalculator

class SimpleAppCalculatorExtender(SimpleAppCalculator):

    def divition(self, first_number, second_number):
        answer = first_number / second_number
        print(answer)