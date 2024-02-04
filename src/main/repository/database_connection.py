from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from src.main.repository.database_settings import DatabaseSettings

class DatabaseConnection:
    def __init__(self, settings: DatabaseSettings):
        self.engine = create_engine('sqlite:///torturapp.db')
        self.session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_db(self) -> Session:
        db = self.session_local()
        try:
            yield db
        finally:
            db.close()