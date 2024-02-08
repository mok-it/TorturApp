from typing import List

from src.main.logic.block import Block
from src.main.logic.exercise import Exercise
from src.main.logic.group import Group
from src.main.logic.information import Information


class Logic:
    blocks: List[Block] = []
    groups: List[Group] = []
    settings = Information()

    def add_group(self, group: Group) -> None:
        self.groups.append(group)

    def create_blocks(self, blocks_length: List[int], min_good_sols: List[int]) -> None:
        for block_length in blocks_length:
            self.blocks.append(Block(block_length,
                               [Exercise(None) for _ in range(0, block_length)],
                               [min_good_sol for min_good_sol in min_good_sols]))

    def get_num_of_groups(self) -> int:
        return len(self.groups)

    def get_nth_block(self, n: int) -> Block:
        assert len(self.blocks) > n >= 0
        return self.blocks[n]

    def create_n_groups(self, n: int):
        self.groups.clear()
        for i in range(0, n):
            self.add_group(Group([], self.blocks))

    def set_nth_exercise_solution(self, n: int, value: str) -> None:
        block_counter: int = 0
        while n > len(self.blocks[block_counter].exercises):
            n -= len(self.blocks[block_counter].exercises)
            block_counter += 1
        self.blocks[block_counter].exercises[n-1].solution = value

    def sum_exercises(self) -> int:
        return sum([block.size for block in self.blocks])