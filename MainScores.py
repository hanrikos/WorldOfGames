from flask import Flask, render_template_string, render_template
from Score import get_score
from Utils import BAD_RETURN_CODE

"""
This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with
HTML. This will be done by using python’s flask library.
"""

app = Flask(__name__)

SCORE = get_score()

result_html_template = f"""
<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1>The score is <div id="score">{SCORE}</div></h1>
    </body>
</html>
"""

error_html_template = f"""
<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1><div id="score" style="color:red">{BAD_RETURN_CODE}</div></h1>
    </body>
</html>
"""


def page_not_found(e):
    return render_template_string('404.html'), 404


@app.route('/')
def static_file():
    return render_template_string(result_html_template)


def score_server():
    pass


app.run(debug=True)
