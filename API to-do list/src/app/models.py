from app import db

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), index=True, unique=False)
    state = db.Column(db.String(64), index=True, unique=False)
    
    def __repr__(self):
        return f'<Tasks {self.title}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'state': self.state
        }

