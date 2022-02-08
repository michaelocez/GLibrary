from flask import Flask, render_template, redirect, abort
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
loginTest = LoginManager(app)
loginTest.login_view = 'login'


@app.route('/')
def home():
    return render_template("home.html", page_title="Home")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
