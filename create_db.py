from app import app, db

with app.app_context():
    db.create_all()
    print("Database created.")
# This script creates the database and tables defined in the Flask app.