from Live import load_game, welcome
from Score import add_score
print(welcome("Guy"))

result, difficulty = load_game()
if result:
    add_score(difficulty)

