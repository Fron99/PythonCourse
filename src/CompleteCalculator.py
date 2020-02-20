
def menu():
    option = 'J'
    print('Hello to the complete calculator')
    while option != 'Y' and option != 'N':
        option = input('Insert Y if you want execute the calculator or N if you want leave: ').upper()
    return option[0]


def readNumber():
    number = int(input('Insert the number: '))
    return number


def readOption():
    option = 8
    while option < 0 or option > 3:
        print('Options:\n0.- Addition\n 1.- Subtract\n 2.- Divide\n 3.- Multiply')
        option = int(input('Insert the number of the option do you want execute: '))
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

print('Thank for execute my calculate')
print('GoodBye!!!')
