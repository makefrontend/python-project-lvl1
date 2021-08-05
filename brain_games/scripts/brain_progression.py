from brain_games.cli import welcome_user
import random
import prompt


PROGRESSION_LENGHT = 10
NUMBERS_ROUND = 3
MIN_NUMBER = 1
MAX_NUMBER = 20
MIN_DIFFERENCE = 1
MAX_DIFFERENCE = 10
MIN_INDEX = 0
MAX_INDEX = PROGRESSION_LENGHT - 1


def get_progression(initial_value, difference):
    member_progression = initial_value
    progression = [initial_value]
    for i in range(PROGRESSION_LENGHT):
        member_progression += difference
        progression.append(member_progression)
    return progression


def replace_value_from_progression(progression, random_value):
    edit_progression = []
    for i in range(0, PROGRESSION_LENGHT):
        edit_progression.append(str(progression[i]))
    edit_progression[random_value] = '..'
    return " ".join(edit_progression)


def run_game_progression():
    user_name = welcome_user()
    print('What number is missing in the progression?')
    count_round = 0
    while count_round < NUMBERS_ROUND:
        initial_value = random.randrange(MIN_NUMBER, MAX_NUMBER)
        difference = random.randrange(MIN_DIFFERENCE, MAX_DIFFERENCE)
        random_value = random.randrange(MIN_INDEX, MAX_INDEX)
        progression = get_progression(initial_value, difference)
        question = replace_value_from_progression(progression, random_value)
        print(f"Question: {question}")
        answer = prompt.integer('Your answer: ')
        if answer == progression[random_value]:
            print('Correct!')
            count_round += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'. "
                  "\nLet's try again, {}!"
                  .format(answer, progression[random_value], user_name))
            return
    print(f'Congratulations, {user_name}!')


def main():
    run_game_progression()


if __name__ == '__main__':
    main()
