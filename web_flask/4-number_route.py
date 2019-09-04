#!/usr/bin/python3
"""module web_flask Is it a number?"""

from flask import Flask, escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hi():
    return "Hello HBNB!"


@app.route("/hbnb")
def hello():
    return "HBNB"


@app.route("/c/<text>")
def func(text):
    text = text.replace("_", " ")
    return "C {}".format(text).replace("_", " ")


@app.route("/python")
@app.route("/python/<text>")
def coolpython(text="is cool"):
    return "Python {}".format(text).replace("_", " ")


@app.route("/number/<int:n>")
def num(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
