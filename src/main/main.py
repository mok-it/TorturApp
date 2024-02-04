from src.main.model import settings
from src.main.repository.database_connection import DatabaseConnection
from src.main.repository.database_settings import DatabaseSettings
from src.main.view.main_window import window

def main():
    window()

    # start the db connection
    DatabaseConnection(settings=DatabaseSettings())


if __name__ == "__main__":
    main()
