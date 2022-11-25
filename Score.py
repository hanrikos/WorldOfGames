"""
A package that is in charge of managing the scores file.
The scores file at this point will consist of only a number. That number is the accumulation of the
winnings of the user. Amount of points for winning a game is as follows:
POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
Each time the user is winning a game, the points he one will be added to his current amount of
point saved in a file.
"""


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5

    with open('Scores.txt', 'r') as f:
        current_score = f.read()
        new_score = int(current_score) + points_of_winning

    with open('Scores.txt', 'w') as f:
        f.write(str(new_score))

    return new_score


def get_score():
    scores_file = open('Scores.txt', 'r')
    return scores_file.readline()

