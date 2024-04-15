from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DbLink(object):
    """This class knows how to connect to the database."""

    def __init__(self):
        engine = create_engine('sqlite:///torturapp.db', echo=True)
        self.session_registry = sessionmaker(bind=engine)
        

    @contextmanager
    def CommittingSession(self, **kwargs):
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
            self.session_registry.remove()