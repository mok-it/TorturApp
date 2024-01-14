from typing import List

from src.main.logic.block import Block
from src.main.logic.exercise import Exercise
from src.main.logic.group import Group


class Logic:
    blocks: List[Block] = []
    groups: List[Group] = []

    def __init__(self):
        pass

    def addGroup(self, group: Group) -> None:
        self.groups.append(group)

    def createBlocks(self, blocks_length: List[int]) -> None:
        for block_length in blocks_length:
            self.blocks.append(Block(block_length, [Exercise(None) for _ in range(0, block_length)]))

    def getNthBlock(self, n: int) -> Block:
        assert len(self.blocks) > n >= 0
        return self.blocks[n]

    def sumBlocksLength(self):
        return sum([block.size for block in self.blocks])