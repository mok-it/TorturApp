from src.main.repository.database_connection import setup_database
from src.main.view.main_window import window


def main():
    setup_database()
    window()
    

if __name__ == "__main__":
    main()
