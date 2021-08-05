import random
import prompt


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBERS_ROUND = 3
MIN_NUMBER = 1
MAX_NUMBER = 50


def even():
    print('Welcome to the Brain Games! ')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    print(GAME_DESCRIPTION)
    count_round = 0
    while count_round < NUMBERS_ROUND:
        number_rundom = random.randrange(MIN_NUMBER, MAX_NUMBER)
        print(f"Question {number_rundom}")
        number_answer = prompt.string('Your answer: ')
        if (number_rundom % 2 == 0 and number_answer == 'yes') \
                or (number_rundom % 2 == 1 and number_answer == 'no'):
            print('Correct!')
        else:
            print("Let's try again")
            return
        count_round += 1
    print(f"Congratulations, {player_name}!!!")


def main():
    even()


if __name__ == '__main__':
    main()
