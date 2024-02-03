from enum import Enum
from typing import List

from src.main.logic.exercise import Exercise


class Solution(Enum):
    RIGHT = 1
    WRONG = 0


class GroupExercise(Exercise):
    answers: List[Solution] = []

    def __init__(self, solution):
        super().__init__(solution)
        self.answers = []

    def answer_exercise(self, answer: Solution) -> None:
        self.answers.append(answer)

    def get_answers(self) -> List[Solution]:
        return self.answers

    def get_nth_answer(self, n: int) -> Solution:
        return self.answers[n]

    def get_last_good_answer(self) -> int:
        if len(self.answers) == 0 or self.answers[-1] == Solution.WRONG:
            return -1
        index: int = len(self.answers) - 1
        while self.answers[index] == Solution.RIGHT and index >= 0:
            index -= 1
        return index+1