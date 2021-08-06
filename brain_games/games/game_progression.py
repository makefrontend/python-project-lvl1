import random


GAME_DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGHT = 10
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


def round_game():
    initial_value = random.randrange(MIN_NUMBER, MAX_NUMBER)
    difference = random.randrange(MIN_DIFFERENCE, MAX_DIFFERENCE)
    random_value = random.randrange(MIN_INDEX, MAX_INDEX)
    progression = get_progression(initial_value, difference)
    question = replace_value_from_progression(progression, random_value)
    return question, str(progression[random_value])
