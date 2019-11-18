from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import settings

app = Flask(__name__)
app.config.from_object("settings")
db = SQLAlchemy(app)


@app.route('/')
def login():
    return render_template("login.html")