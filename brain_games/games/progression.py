from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_START_NUMBER = -100
MAX_START_NUMBER = 100
START_STEP = 1
END_STEP = 100
MAX_NUMBER = 100
MIN_LENGTH = 5
MAX_LENGTH = 10


def get_progression(start, step, length):
    items = []
    for i in range(length):
        items.append(start + i * step)

    return items


def generate_round():
    start = randint(MIN_START_NUMBER, MAX_START_NUMBER)
    step = randint(START_STEP, END_STEP)
    length = randint(MIN_LENGTH, MAX_LENGTH)

    progression = get_progression(start, step, length)

    hidden_index = randint(0, length - 1)
    answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join([str(item) for item in progression])

    return question, answer
