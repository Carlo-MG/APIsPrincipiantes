from flask import Flask, request, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

# Usuarios y contraseñas simuladas
users = {
    "user1": "password1",
    "user2": "password2"
}

def check_auth(username, password):
    """Verifica si un nombre de usuario y contraseña son válidos."""
    return username in users and users[username] == password

def authenticate():
    """Envía una respuesta 401 para que el cliente proporcione credenciales."""
    return Response(
        'No estás autenticado. Por favor, proporciona tus credenciales.\n'
        'Para loguearte, usa "user1" y "password1".\n',
        401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

def requires_auth(f):
    """Decorador para rutas que requieren autenticación."""
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def public_route():
    return "Esta es una ruta pública."

@app.route('/protected')
@requires_auth
def protected_route():
    return "Has accedido a una ruta protegida."

if __name__ == '__main__':
    app.run(debug=True)
