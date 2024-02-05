from src.main.logic.exercise import Exercise
from typing import List


class Block:
    exercises: List[Exercise] = []
    min_good_solutions: List[int] = []
    size: int

    def __init__(self, size: int, exercises: List[Exercise], min_good_sol: List[int]):
        self.size = size
        self.exercises = exercises
        self.min_good_solutions = min_good_sol

    def get_exercises(self) -> List[Exercise]:
        return self.exercises

    def get_nth_exercise(self, n: int) -> Exercise:
        if n < 0 or n >= self.size:
            raise IndexError("Index out of list")
        return self.exercises[n]