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
    for _ in text:
        if _ == '_':
            print(" ")
    return f"C {text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
