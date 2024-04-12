import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from src.main.repository.database_connection import setup_database
from src.main.view.main_window import window


def main():
    # Call the table initializer
    setup_database()
    window()
    

if __name__ == "__main__":
    main()
