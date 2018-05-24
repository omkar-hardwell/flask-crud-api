"""Database connection."""
import configs

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Create engine, session and base declarative
engine = create_engine(configs.DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
