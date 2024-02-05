from src.main.api.api import API
from src.main.logic.logic import Logic
from src.main.view.main_window import window


def main():
    logic = Logic()
    api = API(logic)
    window(api)


if __name__ == "__main__":
    main()
