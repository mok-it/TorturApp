from sqlalchemy.orm import Mapped, mapped_column
from src.main.model.base import Base

class CorrectSolution(Base):
    __tablename__ = "correct_solution"

    id: Mapped[int] = mapped_column(primary_key=True)
    block_number: Mapped[int] = mapped_column() # could be calculated, but it's probably easier to store it - it is necessary when calculating points
    exercise_number: Mapped[int] = mapped_column()
    category: Mapped[str] = mapped_column()
    solution: Mapped[str] = mapped_column() # though uncommon, some exercises might require a string as an answer