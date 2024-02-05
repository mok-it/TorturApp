
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main.model import correct_solution, settings, submission, team

from src.main.model.base import Base

db_file = "torturapp.db"

# SQLite adatbázis létrehozása
engine = create_engine(f"sqlite:///{db_file}")

# Adatbázis táblák létrehozása
Base.metadata.create_all(engine)

# Session létrehozása az adatbázis műveletek végrehajtásához
Session = sessionmaker(bind=engine)
session = Session()
