from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main.model.base import Base
from src.main.model.correct_solution import CorrectSolution
from src.main.model.settings import Settings
from src.main.model.submission import Submission
from src.main.model.team import Team

class Dblink:
    """This class knows how to connect to the database."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Dblink, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        engine = create_engine('sqlite:///torturapp.db', echo=True)
        self.session_registry = sessionmaker(bind=engine)

        Base.metadata.create_all(engine)
        

    @contextmanager
    def committing_session(self, **kwargs):
        """Creates a session, commits at the end, rolls back on exception, removes.

        Args:
          **kwargs: optional; supplied to session_registry while asking
            to construct a session (mostly for testing).

        Yields:
          a session object. The session will .commit() when a `with CommittingSession()`
          statement terminates normally, or .rollback() on an exception.
        """
        try:
            session = self.session_registry(**kwargs)  # this gives us a session.
            # transaction has already begun here, so no explicit .begin().
            yield session
        except:
            session.rollback()
            raise
        else:
            session.commit()
        finally:
            # Note: close() unbinds model objects, but keeps the DB connection.
            session.close()