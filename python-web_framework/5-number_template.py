"""
This is a Flask web application that implements various routes.
"""

from flask import Flask, abort, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns a greeting message "Hello HBNB!" when the root URL is accessed.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns "HBNB" when the URL /hbnb is accessed.
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    Returns "C " followed by the value of the text variable (with underscores replaced by spaces).
    """
    text = text.replace("_", " ")
    return f"C {text}"

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Returns "Python " followed by the value of the text variable (with underscores replaced by spaces).
    """
    text = text.replace("_", " ")
    return f"Python {text}"

@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """
    Returns a message indicating whether n is a number or not.
    """
    if n.isdigit():
        return f"{n} is a number"
    else:
        abort(404)

@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """
    Renders an HTML page that displays the number n.
    """
    if n.isdigit():
        return render_template('./templates/5-number.html', n=n)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)