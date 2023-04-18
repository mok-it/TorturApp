import csv

class Submission:
    nextId = 0;

    def __init__(self, id, teamId, challangeId, isCorrect, createdAt):
        self.id = self.nextId
        self.nextId = self.nextId + 1
        self.teamId = teamId
        self.challangeId = challangeId
        self.isCorrect = isCorrect
        self.createdAt = createdAt





