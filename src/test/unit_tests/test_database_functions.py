import unittest
from src.main.model.team import Team
from src.main.model.correct_solution import CorrectSolution
from src.main.model.settings import Settings, BlockCriteria
from src.main.repository.repository import Repository


class TestRepositoryMethods(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRepositoryMethods, self).__init__(*args, **kwargs)
        self.repo = Repository()
        self.repo.setup_database()

    def test_create_and_get_team(self):
        team_number = "123"
        team = Team(team_number=team_number, category="ABCD", names="Béla,Jenő")
        self.repo.create_team(team)
        db_teams = self.repo.get_teams()
        self.assertIn(team, db_teams)

    def test_create_and_get_correct_solution(self):
        correct_solution = CorrectSolution(block_number=1, exercise_number=1, solution="Test Solution", category="Bocs")
        self.repo.create_correct_solution(correct_solution)
        db_correct_solutions = self.repo.get_correct_solutions()
        self.assertIn(correct_solution, db_correct_solutions)

    def test_create_and_get_settings(self):
        settings = Settings(number_of_excercises=15, number_of_blocks=5,
                            criteria_of_moving_to_next_block=BlockCriteria.FIFTY_PERCENT_PLUS_ONE)
        self.repo.create_settings(settings)
        db_settings = self.repo.get_settings()
        self.assertIn(settings, db_settings)