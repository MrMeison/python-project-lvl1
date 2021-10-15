from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_progression(start, step, length):
    items = []
    for i in range(length):
        items.append(start + i * step)

    return items


def generate_round():
    start = randint(-100, 100)
    step = randint(1, 100)
    length = randint(5, 10)

    progression = get_progression(start, step, length)

    hidden_index = randint(0, length - 1)
    answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join([str(item) for item in progression])

    return question, answer
