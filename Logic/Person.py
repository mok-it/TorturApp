import csv

class Person:
    nextId = 0;

    def __init__(self, teamId, name):
        self.id = self.nextId
        self.nextId = self.nextId + 1
        self.teamId = teamId
        self.name = name

    ##search the teamid for a person







