import prompt


NUMBERS_ROUND = 3


def greet_user():
    print('Welcome to the Brain Games!')


def get_user_name():
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    return user_name


def run_game(game):
    greet_user()
    user_name = get_user_name()
    print(game.GAME_DESCRIPTION)
    for i in range(NUMBERS_ROUND):
        question, result = game.round_game()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'. "
                  "\nLet's try again, {}!".format(answer, result, user_name))
            return
    print(f'Congratulations, {user_name}!')
