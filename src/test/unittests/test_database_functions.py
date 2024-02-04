import unittest

from sqlalchemy.orm import Session
from src.main.model.team import Team
from src.main.repository.database_connection import DatabaseConnection
from src.main.repository.database_settings import DatabaseSettings


class TestDbFunctions(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestDbFunctions, self).__init__(*args, **kwargs)
        db_settings = DatabaseSettings()
        self.db_connection = DatabaseConnection(db_settings)
        self.db: Session = next(self.db_connection.get_db())

    def test_create_and_read_team(self):
        team_number = "123"
        # Create a team
        team = Team(team_number=team_number, category="ABCD")

        # Write it to the database
        self.db.add(team)
        self.db.commit()

        # Read it from the database
        db_team = self.db.query(Team).filter_by(team_number=team_number).first()

        # Assert that the team was correctly written and read from the database
        self.assertEqual(db_team.team_number, team.team_number)
        self.assertEqual(db_team.category, team.category)