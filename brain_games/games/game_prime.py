import random


GAME_DESCRIPTION = 'Answer "yes" if given number is prime. \
                    Otherwise answer "no".'
FIRST_PRIME_NUMBER = 2
MAX_NUMBER = 50


def is_prime(prime_number):
    if prime_number < FIRST_PRIME_NUMBER:
        return False
    for i in range(FIRST_PRIME_NUMBER, prime_number // 2 + 1):
        if prime_number % i == 0:
            return False
    return True


def round_game():
    prime_number = random.randint(FIRST_PRIME_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_prime(prime_number) else 'no'
    return prime_number, answer
