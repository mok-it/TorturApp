from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
import datetime


class Submission:
    nextId = 0

    def __init__(self, teamId, challangeId, isCorrect):
        self.id = self.nextId
        self.nextId = self.nextId + 1
        self.teamId = teamId
        self.challangeId = challangeId
        self.isCorrect = isCorrect
        self.createdAt = datetime.now()



    ## save a new submission





