def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1/n2

while True:
    n1 = float(input('Enter First Number: '))
    n2 = float(input('Enter Second Number: '))
    type = input('Enter Operation: ')
    if type == 'a':
        print(addition(n1, n2))
    elif type == 's':
        print(subtraction(n1, n2))
    elif type == 'm':
        print(multiplication(n1, n2))
    elif type == 'd':
        print(division(n1, n2))
    print()
