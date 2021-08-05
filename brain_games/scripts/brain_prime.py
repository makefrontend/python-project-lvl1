from brain_games.cli import welcome_user
import random
import prompt


NUMBERS_ROUND = 3
FIRST_PRIME_NUMBER = 2
MAX_NUMBER = 50


def is_prime(number):
    if number < FIRST_PRIME_NUMBER:
        return False
    for i in range(FIRST_PRIME_NUMBER, number // 2 + 1):
        return False if (number % i == 0) else True


def run_is_prime():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    coint_round = 0
    while coint_round < NUMBERS_ROUND:
        number = random.randint(FIRST_PRIME_NUMBER, MAX_NUMBER)
        correct_answer = 'yes' if is_prime(number) else 'no'
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            coint_round += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'. "
                  "\nLet's try again, {}!"
                  .format(answer, correct_answer, user_name))
            return
    print(f'Congratulations, {user_name}!')


def main():
    run_is_prime()


if __name__ == '__main__':
    main()
