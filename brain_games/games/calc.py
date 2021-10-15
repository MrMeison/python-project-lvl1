from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'
OPERATORS = ('+', '-', '*')


def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def generate_round():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    operator = choice(OPERATORS)
    question = '{} {} {}'.format(num1, operator, num2)
    answer = str(calculate(num1, num2, operator))

    return question, answer
