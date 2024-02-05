from sqlalchemy.orm import Session
from src.main.model import team, submission

class Repository:
    _instance = None

    # making the class a singleton
    def __new__(cls, session: Session):
        if cls._instance is None:
            cls._instance = super(Repository, cls).__new__(cls)
            cls._instance.session = session
        return cls._instance

    def create(self, instance):
        self.session.add(instance)
        self.session.commit()
        return instance

    def read(self, model, filter_by):
        return self.session.query(model).filter_by(**filter_by).first()

    def update(self, instance, **kwargs):
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        self.session.commit()
        return instance

    def delete(self, instance):
        self.session.delete(instance)
        self.session.commit()