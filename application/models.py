from application import db, login_manager
from flask_login import UserMixin


class collections(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    itemslist_id = db.Column(db.Integer, db.ForeignKey('itemslist.id'), nullable=False)
    drmartens_id= db.Column(db.Integer, db.ForeignKey('drmartens.id'), nullable=False)

def __repr__(self):
    return ''.join([
        'DocID: ', drmartens.drmartens_id, '\r\n',
        'ItemID: ', itemslist.itemslist_id, '\r\n'
    ])

class drmartens(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    style_code = db.Column(db.Integer, nullable=False, unique=True)
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), nullable=False)
    itemslist_id = db.Column(db.Integer, db.ForeignKey('itemslist.id'), nullable=False)
    
def __repr__(self):
    return ''.join([
     'ItemID: ', itemslist.itemslist_id, '\r\n'   
    ])

class itemslist(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), nullable=False)
    drmartens_id = db.Column(db.Integer, db.ForeignKey('drmartens.id'), nullable=False)
    
def __repr__(self):
    return ''.join([
     'ItemID: ', drmartens.drmartens_id, '\r\n'   
    ])

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

