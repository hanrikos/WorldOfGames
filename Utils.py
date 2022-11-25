import os
"""
A general purpose python file. This file will contain general information and operations we need
for our games.
"""

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 1


def screen_cleaner():
    os.system('clear')
