from app import app
from models import db, Pet
from forms import PetForm, EditPetForm
from unittest import TestCase

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///pet_test'
app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False


db.drop_all()
db.create_all()


class FormsTestCase(TestCase):

    def setUp(self):

        Pet.query.delete()

        pet =  Pet(name="lucky", species="dog", photo_url="https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-800x825.jpg",age=5, notes="Very Cute Dog", available=True)

        db.session.add(pet)
        db.session.commit()

        self.pet_id = pet.id

    def tearDown(self):

        db.session.rollback()

    def test_add_form(self):
        with app.test_client() as client:
            resp = client.get("/pets/add")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form id="add-pet-form"', html)
    

    def test_edit_form(self):
        with app.test_client() as client:
            resp = client.get(f"/pets/{self.pet_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form id="edit-pet-form"', html)


class PostRequestsTestCase(TestCase):

    def setUp(self):

        Pet.query.delete()

        pet =  Pet(name="lucky", species="dog", photo_url="https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-800x825.jpg",age=5, notes="Very Cute Dog", available=True)

        db.session.add(pet)
        db.session.commit()

        self.pet_id = pet.id

    def tearDown(self):

        db.session.rollback()

    
    def test_add_pet(self):
        with app.test_client() as client:
            data = {"name": "Rose", "species": "cat", "photo_url": "https://i.natgeofe.com/n/46b07b5e-1264-42e1-ae4b-8a021226e2d0/domestic-cat_thumb_square.jpg", "age": "2", "available": False}
            resp = client.post("/pets/add", data=data, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Rose", html)


    def test_edit_pet(self):
        with app.test_client() as client:
            data = {"photo_url": "https://i.natgeofe.com/n/46b07b5e-1264-42e1-ae4b-8a021226e2d0/domestic-cat_thumb_square.jpg", "notes": "Cute Cat", "available": True}
            resp = client.post(f"/pets/{self.pet_id}", data=data, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("https://i.natgeofe.com/n/46b07b5e-1264-42e1-ae4b-8a021226e2d0/domestic-cat_thumb_square.jpg", html)
