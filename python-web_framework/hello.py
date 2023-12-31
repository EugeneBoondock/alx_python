from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
    'author': 'Eugene',
    'content': 'poetry',
    'date_posted': '15 August 2035',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
