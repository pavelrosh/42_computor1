from sys import argv
from re import findall

allowed_symbols = ['X', '+', '-', '=', '^', '*', '.']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['+', '-', '=']


def is_term(term: str) -> bool:
    if '*' in term and 'X' in term:
        number = term.split('*')
        try:
            float(number[0])
            if findall(r'X\^[0-2]', number[1]) or number[1] == 'X':
                return True
        except ValueError:
            # print(f'{number} Not a Term')
            return False
    elif term == 'X' or term == 'X^2':
        return True
    else:
        return False


def is_number(number: str) -> bool:
    try:
        float(number)
        # print(f"{number} is Number")
        return True
    except ValueError:
        # print(f'{number} NOT A NUMBER')
        return False


def check_lexicon(equation: str) -> bool:
    # TODO check that max pox not more than 2.
    if '=' in equation and any(i in equation for i in numbers) and any(i for i in allowed_symbols):
        if equation.replace(' ', ''):
            for i in equation.replace(' ', ''):
                if i not in allowed_symbols + numbers:
                    return False
            return True
        else:
            return False
    else:
        return False


def check_syntax(equation: str) -> bool:
    equation = equation.replace(' * ', '*').split(' ')

    for i in range(len(equation)):
        if is_number(number=equation[i]) or is_term(term=equation[i]):
            # print(i)
            # print(f"number or term: {equation[i]}")
            # check if not last item
            if i != len(equation) - 1:
                if equation[i + 1] in symbols:
                    continue
            else:
                return True
        elif equation[i] in symbols:
            # if not first or last symbol
            if i != 0 and i != len(equation) - 1:
                # if item is -, +, = check next or previous symbol should be a term.
                if is_number(equation[i - 1]) or is_term(term=equation[i - 1]) or is_number(number=equation[i + 1]) or is_term(term=equation[i + 1]):
                    continue
                else:
                    print("Wrong position of sign")
                    return False
            else:
                print("Don't put sign at start or finish of equation.")
                return False
        else:
            print(f"Some shit in the input {equation[i]}")
            return False


def get_degree(equation: str):
    degree = []
    equation = equation.replace(' * ', '*')
    equation = equation.split(' ')
    # print(equation)
    for i in equation:
        if findall(r'X\^[0-2]', i):
            term = i.split('^')
            degree.append(term[-1])
        elif i == 'X':
            degree.append('1')
    degree.sort()
    print(f"Polynomial degree: {degree[-1]}")
    # return degree[-1]


def parser():
    if len(argv) == 1:
        print("You didn't put any parameter!")
    elif len(argv) > 2:
        print("Too many parameters!")
    else:
        equation = argv[1]
        if check_lexicon(equation=equation) and check_syntax(equation=equation):
            return True
        else:
            return False
