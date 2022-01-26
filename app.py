from flask import Flask, render_template, redirect
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app =Flask(__name__)
app.config["SECERT_KEY"] = "QWEFBSU8812341A"
# app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def home_page():
    """Shows home page"""
    pets = Pet.query.all()
    return render_template("home_page.html", pets=pets)