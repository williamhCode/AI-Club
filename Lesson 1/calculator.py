def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1/n2

while True:
    n1 = int(input('Enter First Number: '))
    n2 = int(input('Enter Second Number: '))
    type = input('Enter Operation: ')
    if type == '+':
        print(addition(n1, n2))
    elif type == '-':
        print(subtraction(n1, n2))
    elif type == '*':
        print(multiplication(n1, n2))
    elif type == '/':
        print(division(n1, n2))
    print()
