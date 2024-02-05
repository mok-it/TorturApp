from typing import List

from src.main.logic.group import Group
from src.main.logic.logic import Logic


class API:
    def __init__(self, logic: Logic):
        self.logic = logic

    def set_camp(self, camp: str) -> None:
        self.logic.settings.set_camp(camp)

    def set_age(self, age: str) -> None:
        self.logic.settings.set_age(age)

    def set_blocks(self, blocks: List[int], min_good_sol: int, min_good_sols: List[int]) -> None:
        # min_good_sol:
        # 0 : 50% + 1
        # 1 : 50%
        # 2 : custom
        self.logic.blocks.clear()
        if min_good_sol == 0:
            self.logic.create_blocks(blocks, [(num // 2) + 1 for num in blocks])
        elif min_good_sol == 1:
            self.logic.create_blocks(blocks, [(num // 2) for num in blocks])
        elif min_good_sol == 2:
            self.logic.create_blocks(blocks, min_good_sols)

    def set_manual_letting(self, manual_letting: bool) -> None:
        self.logic.settings.set_manual_letting(manual_letting)

    def set_groups_file(self, groups_file_path: str) -> None:
        self.logic.settings.set_groups_file_path(groups_file_path)

    def set_solutions_file(self, solutions_file_path: str) -> None:
        self.logic.settings.set_solutions_file_path(solutions_file_path)

    def check_solution_file(self, file) -> int:
        try:
            f = open(file, "r")
            exercise_number = 0
            for line in f:
                if line.rstrip() != "":
                    exercise_number += 1
            if exercise_number != self.logic.sum_exercises():
                return 1
        except:
            return 2
        return 0

    def read_groups_file(self) -> None:
        f = open(self.logic.settings.groups_file_path, "r")
        group = []
        for line in f:
            if line.rstrip() == "":
                self.logic.add_group(Group(group, self.logic.blocks))
                group.clear()
            else:
                group.append(line.rstrip())
        f.close()

    def read_solution_file(self) -> None:
        f = open(self.logic.settings.solutions_file_path, "r")
        counter: int = 0
        for line in f:
            if line.rstrip() != "":
                self.logic.set_nth_exercise_solution(counter, line.rstrip())
                counter += 1
        f.close()
