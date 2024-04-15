from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.main.model.base import Base

class Submission(Base):
    __tablename__ = "submission"

    id: Mapped[int] = mapped_column(primary_key=True)
    block_number: Mapped[int]
    exercise_number: Mapped[int]
    answer: Mapped[str] # though uncommon, some exercises might require a string as an answer
    team_id: Mapped[int] = mapped_column(ForeignKey('team.id'))

    team = relationship("Team", back_populates="submissions")

    def __str__(self):
        return f"Submission(id={self.id}, block_number={self.block_number}, exercise_number={self.exercise_number}, answer={self.answer}, team_id={self.team_id})"