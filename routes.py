from flask import Flask, render_template, redirect, abort, flash, url_for, request
from flask_login import LoginManager, logout_user, login_user, current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegistrationForm
import models

app = Flask(__name__)

app.config['SECRET_KEY'] = '18197'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Glibrary.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app = 'login'

@login_manager.user_loader
def load_user(id):
    return models.User.query.get(int(id))

@app.route('/')
def home():
    return render_template("home.html", title="Home")

@app.route('/games')
def games():
    return render_template("games.html", games=games, title="Games")

@app.route('/developers')
def developers():
    return render_template("developers.html", developer = developer,
     title="Developers")

@app.route('/about')
def about():
    return render_template("about.html", title="About")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Incorrect Password')
        else:
            login_user(user, remember=form.remember_me.data)
        flash('Logged in successfully.')
        next = request.args.get('next')
        return redirect(next or url_for('home'))
    return render_template('login.html', form=form, title="Login")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = models.User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now a registered user.')
        return redirect(url_for('login'))
    return render_template("register.html", form=form, title="Register")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.errorhandler(404)
def error404(error):
    return render_template('404.html', title='Error'), 404



if __name__ == "__main__":
    app.run(debug=True, port=8080)
