from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.orm import sessionmaker

from src.main.model import settings
from src.main.model.base import Base

from src.main.model.team import Team
from src.main.model.correct_solution import CorrectSolution
from src.main.model.settings import Settings
from src.main.model.submission import Submission
class DatabaseConnection:
    def __init__(self):
        self.engine = create_engine('sqlite:///torturapp.db', echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
    def setup_database(self):
        # engine = create_engine('sqlite:///torturapp.db', echo=True)
    
        Base.metadata.create_all(self.engine)
        # Session = sessionmaker(bind=engine)
        # session = Session()
        
        # Uncomment this to add some data to the database
        # teams = [
        #     Team(team_number="1", category="Bocs", names="Bela,Aladar"),
        #     Team(team_number="2", category="Bocs", names="Geza,Kata"),
        #     Team(team_number="3", category="Jeges", names="Jani,Zoli"),
        # ]
        # 
        # setting1 = Settings(number_of_blocks=10, number_of_excercises=20,  
        #                      criteria_of_moving_to_next_block=settings.BlockCriteria.FIFTY_PERCENT_PLUS_ONE)
        # 
        # correct_solutions = [
        #     CorrectSolution(block_number=1, exercise_number=1, category="Bocs", solution="1"),
        #     CorrectSolution(block_number=2, exercise_number=2, category="Jeges", solution="212")
        # ]
        # 
        # session.add_all(teams)
        # session.add(setting1)
        # session.add_all(correct_solutions)
        self.session.commit()
        self.session.close()

    def create_submission_for_team_with_id(self, team_id: int):

        team = select(Team).where(Team.id == id)
        print("tried to query team")
        if team is not None:
            print("got team")
            submission = Submission(block_number=1, exercise_number=1, answer="Test Answer", team_id=team_id)
            self.session.add(submission)
            self.session.commit()
    
            self.session.close()
        
    def get_teams_submissions(self, team_id: int):
        submissions = select(Submission).where(Submission.team_id == team_id)
        result = self.session.execute(submissions)
        for user_obj in result.scalars():
            print(f"{user_obj.answer} {user_obj.block_number}")
        return result.scalars()
