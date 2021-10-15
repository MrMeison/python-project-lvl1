from random import randint, choice

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

def generate_round():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    question = '{} {}'.format(num1, num2)
    answer = str(gcd(num1, num2))

    return question, answer
