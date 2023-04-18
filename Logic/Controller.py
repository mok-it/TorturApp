import csv

from Logic.Challange import Challange
from Logic.Person import Person
from Logic.Submission import Submission
from Logic.Team import Team


class Controller:
    def __init__(self):
        self.people = []
        with open("Person.csv", 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                values = row.split(" ")
                person = Person(values[0], values[1], values[2])
                self.people.append(person)

        self.challanges = []
        with open("Challange.csv", 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                values = row.split(" ")
                challange = Challange(values[0], values[1])
                self.challange.append(challange)

        teams = []
        with open("Team.csv", 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                values = row.split(" ")
                team = Team(values[0], values[1])
                self.teams.append(team)

        self.submissions = []
        with open("Submission.csv", 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                values = row.split(" ")
                submission = Submission(values[0], values[1], values[2])
                self.submissions.append(submission)

    def createNewSubmission(self, teamId, challangeId, isCorrect):
        submission = Submission(teamId, challangeId, isCorrect)
        with open("Submissions.csv", "w", newline=' ') as csvfile:
            csv_writer = csv.writer(csvfile, delimeter=" ")
            csv_writer.writerow({submission.teamId, submission.challangeId, submission.isCorrect, submission.isCorrect})
        self.submissions.append(submission)

    def searcTeamIdByName(self, wanted_name):
        for person in self.people:
            if person.name == wanted_name:
                return person.teamId




