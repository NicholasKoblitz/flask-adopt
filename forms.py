from tokenize import Number
from flask_wtf import FlaskForm
from sqlalchemy import String
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf



class PetForm(FlaskForm):

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf("cat", "dog", "porcupine")])
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes")