from brain_games.cli import welcome_user
from operator import mul, sub, add
import random
import prompt


NUMBERS_ROUND = 3
OPERATIONS = ((add, '+'), (sub, '-'), (mul, '*'))


def calc():
    user_name = welcome_user()
    print('What is the result of the expression?')
    count_round = 0
    while count_round < NUMBERS_ROUND:
        number_first = random.randrange(1, 50)
        number_second = random.randrange(1, 50)
        operation, symbol_operation = random.choice(OPERATIONS)
        print(f'Question: {number_first} {symbol_operation} {number_second}')
        answer = prompt.string('Your answer: ')
        result = str(operation(number_first, number_second))
        if answer == result:
            print('Correct!')
            count_round += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'. "
                  "\nLet's try again, {}!".format(answer, result, user_name))
            return
    print(f'Congratulations, {user_name}!')


def main():
    calc()


if __name__ == '__main__':
    main()
