import random


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 50


def is_even(number):
    return number % 2 == 0


def round_game():
    number_rundom = random.randrange(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_even(number_rundom) else 'no'
    return str(number_rundom), str(answer)
