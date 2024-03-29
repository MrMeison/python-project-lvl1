from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 0
MAX_NUMBER = 100


def is_even(num):
    return num % 2 == 0


def generate_round():
    num = randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_even(num) else 'no'
    return str(num), answer
