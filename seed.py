# seed.py
from models import db, Customer
from app import app

with app.app_context():
    print("🔄 Removing previous customer data...")
    Customer.query.delete()

    customers = [
        Customer(
            first_name="Alice",
            last_name="Kamau",
            email="alice.kamau@example.com",
            phone="0712345678",
            gender="Female",
            age="28"
        ),
        Customer(
            first_name="Brian",
            last_name="Otieno",
            email="brian.otieno@example.com",
            phone="0722234567",
            gender="Male",
            age="32"
        ),
        Customer(
            first_name="Cynthia",
            last_name="Njeri",
            email="cynthia.njeri@example.com",
            phone="0745567890",
            gender="Female",
            age="25"
        ),
        Customer(
            first_name="Daniel",
            last_name="Mutiso",
            email="daniel.mutiso@example.com",
            phone="0799988776",
            gender="Male",
            age="40"
        ),
        Customer(
            first_name="Evelyn",
            last_name="Chebet",
            email="evelyn.chebet@example.com",
            phone="0700112233",
            gender="Female",
            age="30"
        ),
    ]

    db.session.add_all(customers)
    db.session.commit()
    print("✅ Seeded 5 customers successfully!")
