from routes import db
from sqlalchemy import ForeignKey, true
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.Text)
    password = db.Column(db.Text, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User{}>'.format(self.email)

class Favourites(db.Model):
    __tablename__ = "Favourites"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('Game.id'))

class Game(db.Model):
     __tablename__ = "Game"
     id = db.Column(db.Integer, primary_key=True, nullable=False)
     name = db.Column(db.Text())
     description = db.Column(db.Text())
     price = db.Column(db.Text())
     rating = db.Column(db.Text())
     image = db.Column(db.Text())

class Game_Genre(db.Model):
    __tablename__ = "Game_Genre"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('Game.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('Genre.id'))

class Game_Developer(db.Model):
    __tablename__ = "Game_Deveoper"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('Game.id'))
    developer_id = db.Column(db.Integer, db.ForeignKey('Developer.id'))

class Developer(db.Model):
    __tablename__ = "Developer"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.Text())
    image = db.Column(db.Text())

class Genre(db.Model):
    __tablename__ = "Genre"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tab = db.Column(db.Text())
