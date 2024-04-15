from src.main.model.submission import Submission
from src.main.repository.repository import Repository
from src.main.view.main_window import window


def main():
    dbc = Repository()
    dbc.setup_database()
    dbc.create_submission(Submission(block_number=1, exercise_number=1, answer="1", team_id=1))
    subs = dbc.get_teams_submissions(1)
    print("submissions:")
    for sub in subs:
        print(f"{sub.team_id} {sub.answer}")
    window()
    

if __name__ == "__main__":
    main()
