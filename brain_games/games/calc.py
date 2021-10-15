from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'
OPERATORS = ('+', '-', '*')
MIN_NUMBER = 0
MAX_NUMBER = 100


def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def generate_round():
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    operator = choice(OPERATORS)
    question = '{} {} {}'.format(num1, operator, num2)
    answer = str(calculate(num1, num2, operator))

    return question, answer
