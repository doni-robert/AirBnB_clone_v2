#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
