from app import app, db
from models import User
from werkzeug.security import generate_password_hash

with app.app_context():
    admin = User(
        name='Admin',
        email='officepc860@gmail.com',
        phone='0123456789',
        password=generate_password_hash('7781RS'),
        is_admin=True
    )
    db.session.add(admin)
    db.session.commit()
    print("Admin user created!")
