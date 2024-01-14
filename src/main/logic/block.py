from src.main.logic.exercise import Exercise
from typing import List


class Block:
    exercises: List[Exercise] = []
    size: int = None

    def __init__(self, size: int, exercises: List[Exercise]):
        self.size = size
        self.exercises = exercises

    def getExercises(self) -> List[Exercise]:
        return self.exercises

    def getNthExercise(self, n: int) -> Exercise:
        if n < 0 or n >= self.size:
            raise IndexError("Index out of list")
        return self.exercises[n]