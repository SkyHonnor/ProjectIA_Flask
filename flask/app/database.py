from models.models import db

def init_database(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()