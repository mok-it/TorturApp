import unittest
from src.main.model.team import Team
from src.main.repository.database_connection import session
from src.main.repository.repository import Repository

class TestDbFunctions(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestDbFunctions, self).__init__(*args, **kwargs)
        self.repo = Repository(session)

    def test_create_and_read_team(self):
        team_number = "123"
        # Create a team
        team = Team(team_number=team_number, category="ABCD")

        # Write it to the database
        self.repo.create(team)

        # Read it from the database
        db_team = self.repo.read(Team, {"team_number": team_number})

        # Assert that the team was correctly written and read from the database
        self.assertEqual(db_team.team_number, team.team_number)
        self.assertEqual(db_team.category, team.category) # TODO this does not work yet

    def test_update_team(self):
        team_number = "123"
        # Create a team
        team = Team(team_number=team_number, category="ABCD")

        # Write it to the database
        self.repo.create(team)

        # Read it from the database
        db_team = self.repo.read(Team, {"team_number": team_number})

        # Update the team
        new_category = "EFGH"
        self.repo.update(db_team, category=new_category)

        # Read it from the database
        db_team = self.repo.read(Team, {"team_number": team_number})

        # Assert that the team was correctly updated
        self.assertEqual(db_team.category, new_category)

    def test_delete_team(self):
        team_number = "123"
        # Create a team
        team = Team(team_number=team_number, category="ABCD")

        # Write it to the database
        self.repo.create(team)

        # Read it from the database
        db_team = self.repo.read(Team, {"team_number": team_number})

        # Delete the team
        self.repo.delete(db_team)

        # Read it from the database
        db_team = self.repo.read(Team, {"team_number": team_number})

        self.assertIsNone(db_team) # TODO this does not work yet