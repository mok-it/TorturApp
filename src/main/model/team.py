from typing import Optional

from sqlalchemy import PickleType
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from src.main.model.base import Base

class Team(Base):
    __tablename__ = "team"

    id: Mapped[int] = mapped_column(primary_key=True)
    team_number: Mapped[str]
    category: Mapped[str] # TODO user should be able to define the categories themselves, i.e. ABCD-KLMN-XYZ or something like that
    names: Mapped[str] # list of names, separated by commas, e.g. "Bela, Aladar"
    submissions = relationship("Submission", back_populates="team")
    time_of_finish: Mapped[Optional[str]]
    
    def __str__(self):
        return f"Team(id={self.id}, team_number={self.team_number}, category={self.category}, names={self.names}, time_of_finish={self.time_of_finish})"