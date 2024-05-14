from app import db

class User(): 
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    username = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(60), index=True)
    
    def __repr__(self):
        return f'<User {self.username} >'
    
    
