import os
import datetime
from flask import Flask, session, request, render_template, flash, logging, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
import csv

from models import *
from create import app

app = Flask(__name__)
os.environ['DATABASE_URL'] = 'postgres://hzepsnqyilfhew:04a425ed8eb86e03d32c6e38b31018b40c0d0dbdaf30d6e5263cb99e827f8da2@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d3d0olie7v9qui'
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
# Session = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    # return render_template("home.html")
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return "PLEASE SUBMIT THE FORM"
    else:
        name = request.form.get("name")
        email = request.form.get("mail")
        password = request.form.get("passw")
        u = user(username=name, email=email, password=password)
        p = user.query.get(email)
        if p is None:
            db.add(u)
            db.commit()
            return render_template("index.html", status="New User", name=name)
        else:
            return render_template("index.html", name="Already registered")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/login/", methods=["GET", "POST"])
def thanks():
    if request.method == "GET":
        return "please enter credientials in home page"
    else:
        email = request.form.get("mail")
        password = request.form.get("passw")
        e = user.query.get(email)
        if e is None:
            print(e)
            return render_template("login.html", message="please enter valid credentails")

        u = user.query.filter_by(email=email).first()
        if u.password != password:
            return render_template("login.html", message="Incorrect password")
        else:
            name = u.username
            return render_template("thanks.html", name=name)
