from flask import Flask, request, jsonify, render_template, redirect, render_template_string, Response, url_for
import os

import GuessGame
import MemoryGame
import CurrencyRouletteGame

result: bool
app = Flask(__name__)


@app.route('/')
def get_username():
    return render_template('welcome.html')


@app.route('/choose_game')
def choose_game():
    username = request.args.get('username')
    print(f"here 2{username}")
    return render_template('choose_game.html', username=username)


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG)."


@app.route('/redirecting')
def redirecting():
    games = request.args.get("operations")
    print(f"games {games}")
    difficulty = request.args.get("options")
    print(f"difficulty {difficulty}")
    return redirect(f"/games/{games}?difficulty={difficulty}")


@app.route('/games/currency')
def currency():
    difficulty = request.args.get("difficulty")
    print(f"currency difficulty {difficulty}")
    return render_template(f"/games/currency.html", difficulty=difficulty)


@app.route('/games/guess')
def guess():
    difficulty = request.args.get("difficulty")
    print(f"guess difficulty {difficulty}")
    return render_template(f"/games/guess.html", difficulty=difficulty)


@app.route('/games/memory')
def memory():
    difficulty = request.args.get("difficulty")
    print(f"memory difficulty {difficulty}")
    return render_template(f"/games/memory.html", difficulty=difficulty)


def load_game():
    global result
    while True:
        try:
            chosen_game = int(input("""Please choose a games to play:\n
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
            game_difficulty = int(input("Please choose games difficulty from 1 to 5:"))
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
    return result, game_difficulty


port = int(os.environ.get('PORT', 5011))
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port=port)
