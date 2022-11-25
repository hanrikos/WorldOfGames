import random
import requests

"""
This games will use the free currency api to get the current exchange rate from USD to ILS, will
generate a new random number between 1-100 a will ask the user what he thinks is the value of
the generated number from USD to ILS, depending on the user’s difficulty his answer will be
correct if the guessed value is between the interval surrounding the correct answer
"""
difficulty: int
random_number = random.randint(1, 100)


def get_money_interval():
    url = 'https://v6.exchangerate-api.com/v6/da6f22af24ae1ec17e9053ce/latest/USD'
    response = requests.get(url)
    data = response.json()

    ils_usd_rate = data["conversion_rates"]["ILS"]
    print(data["conversion_rates"]["ILS"])
    interval = random_number*ils_usd_rate - (5 - difficulty), random_number*ils_usd_rate + (5 - difficulty)
    return interval


def get_guess_from_user(random_number, interval):
    chosen_amount = int(input(f"What do you think? How much {random_number} USD is in ILS: "))
    low, high = interval

    if high >= chosen_amount >= low:
        print(f"Good Guess {chosen_amount} is between {high} and {low}")
        return True
    print(f"Sorry, you are far away.")
    return False


def play(game_difficulty):
    global difficulty
    difficulty = game_difficulty
    interval = get_money_interval()
    result = get_guess_from_user(random_number, interval)
    return result
