from enum import Enum
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column
from src.main.model.base import Base

class BlockCriteria(Enum):
    NO_CRITERIA = 0
    FIFTY_PERCENT = 1
    FIFTY_PERCENT_PLUS_ONE = 2

class Settings(Base):
    __tablename__ = "settings"

    id: Mapped[int] = mapped_column(primary_key=True)
    number_of_excercises: Mapped[int] = mapped_column()
    number_of_blocks: Mapped[int] = mapped_column()
    criteria_of_moving_to_next_block: Mapped[BlockCriteria] = mapped_column(SQLEnum(BlockCriteria), default=BlockCriteria.FIFTY_PERCENT_PLUS_ONE)