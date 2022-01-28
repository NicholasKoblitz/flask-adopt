from unicodedata import name
from flask import Flask, render_template, redirect
from models import db, connect_db, Pet
from forms import PetForm, EditPetForm

app =Flask(__name__)
app.config["SECRET_KEY"] = "QWEFBSU8812341A"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route("/")
def home_page():
    """Shows home page"""
    pets = Pet.query.all()
    return render_template("home_page.html", pets=pets)


@app.route("/pets/add", methods=["GET", "POST"])
def add_pet_form():
    """Adds new pet to database"""

    form = PetForm()
    
    if form.validate_on_submit():
        
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")
        
    else:
        return render_template("add_pet.html", form=form)


@app.route("/pets/<int:pet_id>", methods=["GET", "POST"])
def get_pet_details_and_form(pet_id):
    """Shows the detials page for pet and a from to edit that pet's information"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect("/")

    else:
        return render_template("pet_detatils_and_edit.html", form=form, pet=pet)