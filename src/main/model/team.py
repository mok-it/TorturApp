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
    # names: Mapped[Optional[PickleType]] # TODO does not work yet
    submissions = relationship("Submission", back_populates="team")
    time_of_finish: Mapped[Optional[str]]