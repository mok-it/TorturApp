from sqlalchemy import select

from src.main.model.submission import Submission
from src.main.repository import dblink
from src.main.view.main_window import window

def main():
    window()
    

if __name__ == "__main__":
    main()
