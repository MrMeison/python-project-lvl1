from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def generate_round():
    num = randint(0, 100)
    answer = 'yes' if is_even(num) else 'no'
    return str(num), answer
