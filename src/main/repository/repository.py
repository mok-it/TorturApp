from sqlalchemy import select

from src.main.model.correct_solution import CorrectSolution
from src.main.model.settings import Settings
from src.main.model.submission import Submission
from src.main.model.team import Team
from src.main.repository import dblink
from src.main.repository.dblink import Dblink

    # def setup_database(self):
        # engine = create_engine('sqlite:///torturapp.db', echo=True)

        # Base.metadata.create_all(self.engine)
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
        # self.session.commit()
        # self.session.close()