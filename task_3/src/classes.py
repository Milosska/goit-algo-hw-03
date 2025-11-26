from typing import Callable
from src.exceptions import ValueIsNotValidException

class HanoiTower():
    def __init__(self, max_height: int):
        self.__validate_max_height(max_height)
        self.__towers: dict[str, list[int]] = {'A': list(range(max_height, 0, -1)), 'B': [], 'C': []}

    @property
    def towers(self):
        return self.__towers
    
    def get_axes(self) -> list[str]:
        return list(self.towers.keys())
    
    def __validate_max_height(self, max_height: int) -> None:
        if not isinstance(max_height, int):
            raise ValueIsNotValidException()

    def move_disk(self, from_axe: str, to_axe:str) -> None:
        if len(self.towers[from_axe]) > 0:
            disk_to_move = self.towers[from_axe].pop()
            self.towers[to_axe].append(disk_to_move)
            print(f"Disk {disk_to_move} is moved from axe {from_axe} to axe {to_axe}")

    def move_towers(self, discs_to_move: int, base_axe: str, aux_axe: str, target_axe: str) -> None:
        if discs_to_move == 1:
            self.move_disk(base_axe, target_axe)
            return

        self.move_towers(discs_to_move - 1, base_axe, target_axe, aux_axe)
        self.move_disk(base_axe, target_axe)
        self.move_towers(discs_to_move - 1, aux_axe, base_axe, target_axe)
    


        
        


            







