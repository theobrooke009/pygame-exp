should_calculate = 'Y'

while should_calculate == 'Y' or should_calculate == 'y':
    first_number = float(input('What is the first number? '))
    second_number = float(input('What is the second number? '))
    operator = input('Would you like to +,-,/ or * ? ')

    if operator == '+':
        print(first_number + second_number)
    elif operator == '-':
        print(first_number - second_number)
    elif operator == '/':
        print(first_number / second_number)
    elif operator == '*':
        print(first_number * second_number)
    else:
        print('Invalid Operator')

    should_calculate = input('Another Calcultion? enter Y or N ')

print('Thanks for using the Python Calulator, GoodBye')

