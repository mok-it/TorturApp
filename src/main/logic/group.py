from typing import List

from src.main.logic.block import Block


class Group:
    names: List[str] = []
    current_exercise: int = 1
    end_time: str = None
    blocks: List[Block] = []

    def __init__(self, names: List[str], blocks: List[Block]):
        self.names = names
        self.blocks = blocks

    def getCurrentExercise(self):
        i = 0
        sum = self.blocks[0].size
        while sum <= self.current_exercise:
            i += 1
            sum += self.blocks[i].size
        return self.blocks[i].exercises[self.current_exercise - sum - 1]

    def getTotalExercises(self):
        return sum([i.size for i in self.blocks])

    def calculatePoints(self):
        base: List[float] = [0] * (len(self.blocks) + 1)
        points: List[float] = [0] * self.getTotalExercises()
        base[0] = 32
        current_exercise: int = 0
        for block_num in range(0, len(self.blocks)):
            good_answers: int = 0
            for exercise_num in range(0, self.blocks[block_num].size):
                last_good_answer: int = self.blocks[block_num].exercises[exercise_num].getLastGoodAnswer()
                if last_good_answer == -1:
                    points[current_exercise] = 0
                else:
                    points[current_exercise] = pow(2, last_good_answer) * base[block_num]
                    good_answers += 1 if last_good_answer == 0 else 0
                current_exercise += 1
            base[block_num + 1] = base[block_num] + 8 * good_answers
        return sum(points)