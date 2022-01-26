from models import db, Pet
from app import app


db.drop_all()
db.create_all()

Pet.query.delete()

lucky = Pet(name="lucky", species="dog", photo_url="https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-800x825.jpg",age=5, notes="Very Cute Dog", available=True)
rose = Pet(name="Rose", species="cat", photo_url="https://i.natgeofe.com/n/46b07b5e-1264-42e1-ae4b-8a021226e2d0/domestic-cat_thumb_square.jpg", age=2, available=False)
stinky = Pet(name='Mr. Stinky', species="dog", photo_url="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/golden-retriever-royalty-free-image-506756303-1560962726.jpg?crop=0.672xw:1.00xh;0.166xw,0&resize=640:*")

db.session.add_all([lucky, rose, stinky])
db.session.commit()