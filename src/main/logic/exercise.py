class Exercise:
    solution: str

    def __init__(self, solution):
        self.solution = solution

    def get_solution(self) -> str:
        return self.solution

    def get_last_good_answer(self):
        pass
