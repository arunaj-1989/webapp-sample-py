from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'arunaj',
        'title': 'blog title 1',
        'updated': 'November 4, 2021 11:10 AM',
        'content': 'WARNING: This is a beta server. Do not use it in a production deployment.'
    },
    {
        'author': 'Dhanya',
        'title': 'blog title 2',
        'updated': 'November 4, 2021 11:10 AM',
        'content': 'WARNING: This is a Development server. Do not use it in a production deployment.'

    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title=' | contact us')


if __name__ == '__main__':
    app.run(debug=True)
