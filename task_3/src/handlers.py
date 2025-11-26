from src.constants import MIN_ELEMENTS_NUMBER, MAX_ELEMENTS_NUMBER
from src.exceptions import ValueIsNotValidException
from src.decorators import handle_errors
from src.classes import HanoiTower

@handle_errors
def normalize_input(input_str: str) -> str:
    return input_str.lower().strip() 

@handle_errors
def validate_height(input_str: str) -> int:
    if not input_str.isdigit():
        raise ValueIsNotValidException()
    
    int_value = int(input_str)

    if MIN_ELEMENTS_NUMBER > int_value > MAX_ELEMENTS_NUMBER:
        raise ValueIsNotValidException()
    
    return int(input_str)

@handle_errors
def run_hanoi_towers_game(tower_height: int) -> None:
    hanoi_towers = HanoiTower(tower_height)
    print(f"Initial state: {hanoi_towers.towers}")

    tower_axes = hanoi_towers.get_axes()
    discs_to_move = len(hanoi_towers.towers["A"])

    hanoi_towers.move_towers(discs_to_move, tower_axes[0], tower_axes[1], tower_axes[2])
    print(f"Completed! Final state: {hanoi_towers.towers}")

