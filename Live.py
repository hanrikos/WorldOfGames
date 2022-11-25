import GuessGame
import MemoryGame
import CurrencyRouletteGame

result: bool


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG)."


def load_game():
    global result
    while True:
        try:
            chosen_game = int(input("""Please choose a game to play:\n
                    1. Memory Game - a sequence of numbers will appear for 1 second and you have to
                    guess it back\n
                    2. Guess Game - guess a number and see if you chose like the computer\n
                    3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n
                    Here: """))
            if chosen_game <= 0 or chosen_game > 4:
                raise ValueError
            break
        except ValueError:
            print("Invalid integer. The number must be in the range of 1-3.")

    while True:
        try:
            game_difficulty = int(input("Please choose game difficulty from 1 to 5:"))
            if game_difficulty <= 0 or game_difficulty > 5:
                raise ValueError
            break
        except ValueError:
            print("Invalid integer. The number must be in the range of 1-5.")

    print(f"Game {chosen_game} was chosen with difficulty {game_difficulty}")
    if chosen_game == 1:
        result = GuessGame.play(game_difficulty)
    if chosen_game == 2:
        result = MemoryGame.play(game_difficulty)
    if chosen_game == 3:
        result = CurrencyRouletteGame.play(game_difficulty)
    else:
        print("Invalid chose. Lets play guess game")
        result = GuessGame.play(game_difficulty)
    return result, game_difficulty
