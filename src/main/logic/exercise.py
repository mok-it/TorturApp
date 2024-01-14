class Exercise:
    solution: str = None

    def __init__(self, solution):
        self.solution = solution

    def getSolution(self) -> str:
        return self.solution

    def getLastGoodAnswer(self):
        pass
