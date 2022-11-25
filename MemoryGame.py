import random
import sys
import time

"""
The purpose of memory games is to display an amount of random numbers to the users for 0.7
seconds and then prompt them from the user for the numbers that he remember. If he was right
with all the numbers the user will win otherwise he will lose.
"""
difficulty: int


def generate_sequence():
    rand_list = []
    for i in range(difficulty):
        rand_list.append(random.randint(3, 9))
    sys.stdout.write(f"\r{rand_list}")
    time.sleep(2)
    sys.stdout.write("\r")
    return rand_list


def get_list_from_user():
    user_memory_list = []
    print(f"Please enter the {difficulty} numbers you memorized: ")
    for i in range(0, difficulty):
        while True:
            try:
                ele = int(input())
                user_memory_list.append(ele)
            except Exception as e:
                print(f"Please enter integers only, lets start over")
                continue
            else:
                break
    print(user_memory_list)
    return user_memory_list


def is_list_equal(first_list, second_list):
    if sorted(first_list) == sorted(second_list):
        print(f"Congratulations to your memory!")
        return True
    print(f"Sorry, {first_list} and {second_list} are not equal")
    return False


def play(game_difficulty):
    global difficulty
    difficulty = game_difficulty
    rand_list = generate_sequence()
    user_memory_list = get_list_from_user()
    result = is_list_equal(rand_list, user_memory_list)
    return result
