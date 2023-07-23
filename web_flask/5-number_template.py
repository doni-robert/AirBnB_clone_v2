#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ Displays 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ Displays 'HBNB' """
    return "HBNB!"


@app.route('/c/<text>')
def c(text):
    """
    Displays 'C' followed by the text variable with any underscore replaced
    with a space
    """
    return "C " + text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    """
    Displays 'Python' followed by the text variable with any underscore
    replaced with a space
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n):
    """ Dislpays 'n is a number' only if 'n' is an integer """
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Displays a HTML page only if 'n' is an integer """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
