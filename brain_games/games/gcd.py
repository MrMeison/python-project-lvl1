from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 0
MAX_NUMBER = 100


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def generate_round():
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    question = '{} {}'.format(num1, num2)
    answer = str(gcd(num1, num2))

    return question, answer
