from application import db
from application.models import Collections, Drmartens, Itemslist, Users

db.drop_all()
db.create_all()
