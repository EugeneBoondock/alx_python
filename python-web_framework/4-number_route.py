"""
documented again and again
"""
from flask import Flask
"""
This is a flask web application
"""


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function returns a string "Hello BNB!" when the root URL is accessed.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function returns a string "HBNB" when the URL /hbnb is accessed
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    This function returns a string "HBNB" when the URL /hbnb is accessed
    """
    text = text.replace("_", " ")
    return f"C {text}"

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    This function returns a string "HBNB" when the URL /hbnb is accessed
    """
    text = text.replace("_", " ")
    return f"Python {text}"

@app.route('/number/', strict_slashes=False)
@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """
    This function returns a string "HBNB" when the URL /hbnb is accessed
    """
    if n.isdigit():
        return f"{n} is a number"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
