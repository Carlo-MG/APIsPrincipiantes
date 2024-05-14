from src import create_app, db
from src.models import User

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db}
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
