from application import db

class collections(db.Model):
    CollectionID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    DocID = db.Column(db.Integer, db.ForeignKey('drmartens.DocID'), nullable=False)
    ItemsID = db.Column(db.Integer, db.ForeignKey('itemsList.ItemID'), nullable=False)

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])

class drmartens(db.Model):
    DocID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    styleCode = db.Column(db.String(30), nullable=False, unique=True)
    ItemsID = db.Column(db.Integer, db.ForeignKey('itemsList.ItemID'), nullable=False)

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])

class itemsList(db.Model):
    ItemID = db.Column(db.Integer, primary_key=True)
    DocID = db.Column(db.Integer, db.ForeignKey('drmartens.DocID'), nullable=False)
    CollectionID = db.Column(db.Integer, db.ForeignKey('collections.CollectionID'), nullable=False)
    

    def __repr__(self):
        return ''.join([
            'User: ', self.first_name, ' ', self.last_name, '\r\n',
            'Title: ', self.title, '\r\n', self.content
            ])

