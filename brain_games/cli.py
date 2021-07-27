import prompt


def welcom_user():
    user_name = prompt.string('May I have your name? ')
    if user_name != '':
        return user_name
