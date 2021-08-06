import random


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'
NUMBERS_ROUND = 3
MIN_NUMBER = 1
MAX_NUMBER = 20


def get_gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def round_game():
    number_first = random.randrange(MIN_NUMBER, MAX_NUMBER)
    number_second = random.randrange(MIN_NUMBER, MAX_NUMBER)
    question = f'{number_first} {number_second}'
    result = get_gcd(number_first, number_second)
    return question, str(result)
