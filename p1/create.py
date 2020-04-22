import os

from flask import Flask, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

# Import table definitions.
from models import *

app = Flask(__name__)

# Tell Flask what SQLAlchemy databas to use.

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://hzepsnqyilfhew:04a425ed8eb86e03d32c6e38b31018b40c0d0dbdaf30d6e5263cb99e827f8da2@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d3d0olie7v9qui'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the Flask app with the database (no Flask app is actually being run yet).
db.init_app(app)


def main():
    # Create tables based on each table definition in `models`
    db.create_all()


if __name__ == "__main__":
    # Allows for command line interaction with Flask application
    with app.app_context():
        main()
