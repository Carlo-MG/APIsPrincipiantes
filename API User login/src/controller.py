from src.models import User
from src import db

def create_user(data):
    name = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if not name: return {"message":"username undefined"}
    if not email: return {'message':'email undefined'}
    if not password: return 'password undefined'
    
    user = User.query.filter_by(username=name).all()
        
    if user: 
        return {'message':'Nombre en uso'}
    
    user = User.query.filter_by(email=email).all()
    if user: 
        return {'message':'email en uso'}
    
    user = User(username=name, email=email, password=password)
    
    db.session.add(user)
    db.session.commit()
    return {'message':'OK'}
    
def login_by_name(data):
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    if not user: return {'message': 'Nombre de usuario incorrecto'}
    
    if not user.password == password: return {'message': 'Contraseña incorrecta'}
    
    return {'message':'Ok'}

