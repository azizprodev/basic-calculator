# function to get operand
def get_operand(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

# function to get operator
def get_operator():
    while True:
        operator = input("Enter operator (+, -, *, /): ")
        if operator in ['+', '-', '*', '/']:
            return operator
        print("Invalid operator. Please choose among (+, -, *, /)")

# function for calculate values
def calculate(first_operand, operator, second_operand):
    if operator == '+':
        return first_operand + second_operand
    elif operator == '-':
        return first_operand - second_operand
    elif operator == '*':
        return first_operand * second_operand
    elif operator == '/':
        try:
            return first_operand / second_operand
        except ZeroDivisionError:
            print("Error: ZeroDivisionError - In division, the second operand should not be zero.")
            return None

# main function that call all functions
def main():
    while True:
        print("**** Calculator ****")
        first_operand = get_operand("Enter first operand: ")
        operator = get_operator()
        second_operand = get_operand("Enter second operand: ")

        result = calculate(first_operand, operator, second_operand)
        if result is not None:
            print(f"The result of {first_operand} {operator} {second_operand} is: {result}")

        continue_choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            break

# if program is run from main, then execute program
if __name__ == "__main__":
    main()
