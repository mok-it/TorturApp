import unittest

from sqlalchemy import select
from sqlalchemy.orm import session
from src.main.model.team import Team
from src.main.model.correct_solution import CorrectSolution
from src.main.model.settings import Settings, BlockCriteria
from src.main.repository import dblink
from src.main.repository.dblink import Dblink

dblink = Dblink()

class TestRepositoryMethods(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRepositoryMethods, self).__init__(*args, **kwargs)

    def test_create_and_get_team(self):
        with dblink.committing_session() as dbsession:
            team_number = "123"
            team = Team(team_number=team_number, category="ABCD", names="Béla,Jenő")
            dbsession.add(team)
            db_teams = list(dbsession.execute(select(Team)).scalars())
            self.assertIn(team, db_teams)

    def test_create_and_get_correct_solution(self):
        with dblink.committing_session() as dbsession:
            correct_solution = CorrectSolution(block_number=1, exercise_number=1, solution="Test Solution", category="Bocs")
            dbsession.add(correct_solution)
            db_correct_solutions = list(dbsession.execute(select(CorrectSolution)).scalars())
            self.assertIn(correct_solution, db_correct_solutions)

    def test_create_and_get_settings(self):
        with dblink.committing_session() as dbsession:
            settings = Settings(number_of_excercises=15, number_of_blocks=5, criteria_of_moving_to_next_block=BlockCriteria.FIFTY_PERCENT_PLUS_ONE)
            dbsession.add(settings)
            db_settings = list(dbsession.execute(select(Settings)).scalars())
            self.assertIn(settings, db_settings)