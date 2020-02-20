
def menu():
    option = 'J'
    print('Hello to the complete calculator')
    while option != 'Y' and option != 'N':
        print('Insert Y if you want execute the calculator or N if you want leave')
        option = input().upper()
    return option[0]


def readNumber():
    print('Insert the number')
    number = int(input())
    return number


def readOption():
    option = 8
    while option < 0 or option > 3:
        print('Insert the number of the option do you want execute\n'
              '0.- Addition\n'
              '1.- Subtract\n'
              '2.- Divide\n'
              '3.- Multiply')
        option = int(input())
    return option


def switch_optionCalculate(optionCalculate, number1, number2):
    switches = {
        0: number1+number2,
        1: number1-number2,
        2: number1/number2,
        3: number1*number2}
    return switches.get(optionCalculate)




number1 = 0
number2 = 0

option = menu()
optionCalculate = 0
result = 0

while option == 'Y':
    number1 = readNumber()
    number2 = readNumber()
    optionCalculate = readOption()
    result = switch_optionCalculate(optionCalculate,number1,number2)
    print('The result of the calculation is', result)
    option = menu()
