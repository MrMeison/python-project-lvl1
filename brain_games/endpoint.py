import prompt

ROUND_COUNT = 3

def run(game):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)

    name = prompt.string('May I have your name? ')

    i = 0

    while i < ROUND_COUNT:
        question, answer = game.generate_round()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')

        if answer != user_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, answer))
            print("Let's try again, {}!".format(name))
            return

        print('Correct!')
        i += 1

    print('Congratulations, {}!'.format(name))

