from random import randint
"""
The purpose of guess game is to start a new game, cast a random number between 1 to a
variable called difficulty. The game will get a number input from the
"""
difficulty: int


def generate_number():
    secret_number = randint(1, difficulty)
    return secret_number


def get_guess_from_user():
    while True:
        try:
            chosen_number = int(input(f"Please choose number between 1 and {difficulty}:"))
            if chosen_number <= 0 or chosen_number > difficulty:
                raise ValueError
            return chosen_number
        except ValueError:
            print(f"Invalid integer. Please choose number between 1 and {difficulty}")


def compare_results(secret_number, chosen_number):
    if secret_number == chosen_number:
        print(f"Congratulations you hit the bullseye; your chose {chosen_number} "
              f"is equal to secret number {secret_number}")
        return True
    print(f"Sorry, {chosen_number} is not equal to {secret_number}")
    return False


def play(game_difficulty):
    global difficulty
    difficulty = game_difficulty
    chosen_number = get_guess_from_user()
    secret_number = generate_number()
    result = compare_results(chosen_number, secret_number)
    return result
