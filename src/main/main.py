from select import select

from sqlalchemy.orm import Session

from src.main.view.main_window import window
from src.main.model.submission import Submission
from src.main.repository.database_connection import sessionmaker, DatabaseConnection
from src.main.model.team import Team
from sqlalchemy import select

def main():
    dbc = DatabaseConnection()
    dbc.setup_database()
    dbc.create_submission_for_team_with_id(1)
    dbc.get_teams_submissions(1)
    window()
    

if __name__ == "__main__":
    main()
