from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from src.main.model import settings
from src.main.model.base import Base

from src.main.model.team import Team
from src.main.model.correct_solution import CorrectSolution
from src.main.model.settings import Settings
from src.main.model.submission import Submission
def setup_database():
    engine = create_engine('sqlite:///torturapp.db', echo=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    teams = [
        Team(team_number="1", category="Bocs"),
        Team(team_number="2", category="Bocs"),
        Team(team_number="3", category="Jeges")
    ]
    
    setting1 = Settings(number_of_blocks=10, number_of_excercises=20,  
                         criteria_of_moving_to_next_block=settings.BlockCriteria.FIFTY_PERCENT_PLUS_ONE)
    
    correct_solutions = [
        CorrectSolution(block_number=1, exercise_number=1, category="Bocs", solution="1"),
        CorrectSolution(block_number=2, exercise_number=2, category="Jeges", solution="212")
    ]
    
    session.add_all(teams)
    session.add(setting1)
    session.add_all(correct_solutions)
    session.commit()
    session.close()
