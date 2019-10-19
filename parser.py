from sys import argv
from re import findall

allowed_symbols = ['X', '+', '-', '=', '^', '*', '.']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['+', '-', '=']


def is_term(term: str) -> bool:
    if '*' in term and 'X' in term:
        splitted_term = term.split('*')
        if len(splitted_term) == 1 or len(splitted_term) == 2:
            try:
                float(splitted_term[0])
                if len(splitted_term[1]) == 3 and findall(r'X\^[0-2]', splitted_term[1]) or splitted_term[1] == 'X':
                    return True
            except ValueError:
                return False
        else:
            return False
    elif term == 'X' or (findall(r'X\^[0-2]', term) and len(term) == 3):
        return True
    else:
        return False


def is_number(number: str) -> bool:
    try:
        float(number)
        return True
    except ValueError:
        return False


def check_doubles(equation: str):
    equation = ''.join(equation.split())
    if equation.count('=') > 1:
        return False
    i = 0
    while i < len(equation):
        if equation[i] != 'X' and equation[i] in allowed_symbols:
            if i != len(equation) - 1 and equation[i + 1] in ['+', '-']:
                print(equation[i], equation[i+1])
                return False
        i += 1
    return True


def check_lexicon(equation: str) -> bool:
    if '=' in equation and any(i for i in allowed_symbols) and check_doubles(equation=equation):
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
            if findall(r'X\^[3-9]', equation[i]):
                print("The polynomial degree is stricly greater than 2, I can't solve.")
                exit()
            else:
                print(f"Some shit in the input {equation[i]}")
            return False


def get_degree(equation: str):
    degree = []
    equation = equation.replace(' * ', '*')
    equation = equation.split(' ')
    for i in equation:
        if findall(r'X\^[0-2]', i):
            term = i.split('^')
            degree.append(term[-1])
        elif 'X' in i:
            degree.append('1')
    degree.sort()
    print(f"Polynomial degree: {degree[-1]}")
    return int(degree[-1])


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
