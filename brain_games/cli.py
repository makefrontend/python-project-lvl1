import prompt


def welcome_user():
    user_name = prompt.string('May I have your name? ')
    if user_name != '':
        print('Hello, ' + user_name + '!')
        return user_name


def main():
    welcome_user()


if __name__ == '__main__':
    main()
