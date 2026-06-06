from app import create_app
from app.extensions import db
from app.models import User

app = create_app()

with app.app_context():

    admin = User(
        pf_number='ADMIN001',
        full_name='System Admin',
        email='admin@gmail.com',
        role='admin',
        approved=True
    )

    admin.set_password('admin123')

    db.session.add(admin)
    db.session.commit()

    print("Admin created successfully")