from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf



class PetForm(FlaskForm):
    """Form to add pets to the database"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf("cat", "dog", "porcupine")])
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes")

class EditPetForm(FlaskForm):
    """Form to edit pet information"""

    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    notes = TextAreaField("Notes")
    available = BooleanField("Available", validators=[Optional()])
