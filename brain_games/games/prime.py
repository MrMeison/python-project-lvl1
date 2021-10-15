from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 0
MAX_NUMBER = 100


def is_prime(num):
    if num <= 1:
        return False
    divisor = 2
    while divisor <= num // 2:
        if not num % divisor:
            return False
        divisor += 1
    return True


def generate_round():
    num = randint(MIN_NUMBER, MAX_NUMBER)

    answer = 'yes' if is_prime(num) else 'no'

    return str(num), answer
