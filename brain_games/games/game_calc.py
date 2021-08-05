from operator import mul, sub, add
import random


GAME_DESCRIPTION = 'What is the result of the expression?'
OPERATIONS = ((add, '+'), (sub, '-'), (mul, '*'))
MIN_NUMBER = 1
MAX_NUMBER = 50


def round_game():
        number_first = random.randrange(MIN_NUMBER, MAX_NUMBER)
        number_second = random.randrange(MIN_NUMBER, MAX_NUMBER)
        operation, symbol_operation = random.choice(OPERATIONS)
        question = f'{number_first} {symbol_operation} {number_second}'
        result = str(operation(number_first, number_second))
        return question, result