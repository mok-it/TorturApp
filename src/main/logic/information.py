from enum import Enum


class ExerciseType(Enum):
    BLOCK = 0
    EXERCISE = 1


class Information:
    def __init__(self):
        self.camp: str = ""
        self.age: str = ""

        self.exercise_type: ExerciseType = ExerciseType.BLOCK
        self.manual_letting: bool = False

        self.groups_file_path: str = ""
        self.solutions_file_path: str = ""

    def set_camp(self, camp: str):
        self.camp = camp

    def set_age(self, age: str):
        self.age = age

    def set_exercise_type(self, ex_type: ExerciseType):
        self.exercise_type = ex_type

    def set_manual_letting(self, manual_letting: bool):
        self.manual_letting = manual_letting

    def set_groups_file_path(self, groups_file_path: str):
        self.groups_file_path = groups_file_path

    def set_solutions_file_path(self, solutions_file_path: str):
        self.solutions_file_path = solutions_file_path

