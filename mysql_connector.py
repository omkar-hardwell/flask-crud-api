"""Database connection."""
import configs

from src.api import app
from flask_sqlalchemy import SQLAlchemy


# Connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = configs.DATABASE_URI
db = SQLAlchemy(app)
