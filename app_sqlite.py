__author__ = 'hanyuen'

from flask import Flask, render_template,\
    request,redirect, url_for, session, flash, g
from functools import wraps
from flask_sqlalchemy import SQLAlchemy

#import sqlite3

app = Flask(__name__)
app.secret_key = "hano"
#app.database = "mytrains.db"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mytrains.db'
db = SQLAlchemy(app)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("you need to log in first")
            return redirect((url_for("login")))
    return wrap


@app.route("/")
@login_required
def home():
    g.db = connect_db()
    cur = g.db.execute("select * from train")
    trains = [dict(id = row[0], fromCity =row[1], toCity = row[2], size = row[3]) for row in cur.fetchall()]
    g.db.close()
    return render_template("index.html", trains = trains)

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if (request.form["user"] != 'admin' or request.form["password"] != 'admin'):
            error = "Invalid credentials. Please try again"
        else:
            session["logged_in"] = True
            flash("you were just logged in")
            return redirect(url_for('home'))

    return render_template("login.html", error = error)

@app.route("/logout")
@login_required
def logout():
    session.pop('logged_in', None)
    flash("you were just logged out")
    return redirect (url_for("welcome"))

#def connect_db():
#    return sqlite3.connect(app.database)


if __name__ == '__main__':
    app.run(debug=True)