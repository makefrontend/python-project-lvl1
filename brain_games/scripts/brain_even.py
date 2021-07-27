import random
import prompt


NUMBERS_ROUND = 3


def even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_round = 0
    while count_round < NUMBERS_ROUND:
        number_rundom = random.randrange(1, 100)
        print(f"Question {number_rundom}")
        number_answer = prompt.string('Your answer: ')
        if (number_rundom % 2 == 0 and number_answer == 'yes'):
            print('Correct!')
        else:
            print("Let's try again")
            return
        count_round += 1
    print('Congratulations!!!')


even()
