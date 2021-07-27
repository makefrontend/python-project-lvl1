import random
import prompt


NUMBERS_ROUND = 3


def even():
    print('Welcome to the Brain Games! ')
    welcome_name = prompt.string('May I have your name? ')
    print(f'Hello, {welcome_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_round = 0
    while count_round < NUMBERS_ROUND:
        number_rundom = random.randrange(1, 100)
        print(f"Question {number_rundom}")
        number_answer = prompt.string('Your answer: ')
        if (number_rundom % 2 == 0 and number_answer == 'yes') \
                or (number_rundom % 2 == 1 and number_answer == 'no'):
            print('Correct!')
        else:
            print("Let's try again")
            return
        count_round += 1
    print(f"Congratulations, {welcome_name}!!!")


even()
