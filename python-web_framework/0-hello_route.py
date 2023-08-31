"""
documented again and again
"""
from flask import Flask
"""
This is a flask web application
"""


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def app():
    """
    This function returns a string "Hello BNB!" when the root URL is accessed.
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
