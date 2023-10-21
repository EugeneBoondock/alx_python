"""
This is a flask web application
"""
from flask import Flask, abort, render_template

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
    This function returns a string "HBNB" when the URL /hbnb is accessed.
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    This function returns a string "C" followed by the value of text
    """
    text = text.replace("_", " ")
    return f"C {text}"

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    This function returns a string "Python" followed by the value of text
    """
    text = text.replace("_", " ")
    return f"Python {text}"

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    This function returns a string "n is a number" only if n is an integer
    """
    if isinstance(n, int):
        return f"{n} is a number"
    else:
        abort(404)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Renders an HTML page that displays the number n.
    """
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Renders an HTML page that displays if the number n is odd or even.
    """
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
