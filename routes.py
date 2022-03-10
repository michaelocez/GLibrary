from flask import Flask, render_template, redirect, abort, flash
from flask_login import LoginManager, logout_user, login_user, current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegistrationForm
import models

app = Flask(__name__)

app.config['SECRET_KEY'] = '18197'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///GFinder.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def home():
    return render_template("home.html", title="Home")

@app.route('/games')
def games():
    return render_template("games.html", title="Games")

@app.route('/developers')
def developers():
    return render_template("developers.html", title="Developers")

@app.route('/about')
def about():
    return render_template("about.html", title="About")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(user)
        flask.flash('Logged in successfully.')
        next = flask.request.args.get('next')
        if not is_safe_url(next):
            return flask.abort(400)
    return render_template('login.html', title="Login", form=form)

@app.route('/register', methods=['GET', 'POST'])
def signup():
     if current_user.is_authenticated:
         return redirect(url_for('home'))
     form = RegistrationForm()
     if form.validate_on_submit():
        user = models.User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
     return render_template('register.html', title='Sign up', form=form)

@app.errorhandler(404)
def error404(error):
    return render_template('404.html', title='Error'), 404



if __name__ == "__main__":
    app.run(debug=True, port=8080)
