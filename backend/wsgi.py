from flask import Flask
from flask_cors import CORS
from app.db import init_db

def create_app():
    app = Flask(__name__)

    # Enable CORS for all routes
    CORS(app)

    print(f"Initialising the database")
    init_db()
    
    # Import and set up routes
    from app.routes import setup_routes
    setup_routes(app)

    return app
