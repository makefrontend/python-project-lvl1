from brain_games.cli import welcome_user


def welcome():
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print(f"Hello, {user_name}!")


def main():
    welcome()


if __name__ == '__main__':
    main()
