from brain_games.cli import welcome_user
import random
import prompt


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'
NUMBERS_ROUND = 3
MIN_NUMBER = 1
MAX_NUMBER = 20


def get_gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def gcd():
    user_name = welcome_user()
    print(GAME_DESCRIPTION)
    count_round = 0
    while count_round < NUMBERS_ROUND:
        number_first = random.randrange(MIN_NUMBER, MAX_NUMBER)
        number_second = random.randrange(MIN_NUMBER, MAX_NUMBER)
        print(f'Question: {number_first} {number_second}')
        answer = prompt.integer('Your answer: ')
        result = get_gcd(number_first, number_second)
        if answer == result:
            print('Correct!')
            count_round += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'. "
                  "\nLet's try again, {}!".format(answer, result, user_name))
            return
    print(f'Congratulations, {user_name}!')


def main():
    gcd()


if __name__ == '__main__':
    main()
