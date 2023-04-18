class Challange:
    nextId = 0;

    def __init__(self, challangeNumber, solution):
        self.id = self.nextId
        self.nextId = self.nextId + 1
        self.challangeNumber = challangeNumber
        self.solution = solution

    ##read challange




