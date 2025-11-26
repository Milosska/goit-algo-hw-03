from src.constants import MIN_ELEMENTS_NUMBER, MAX_ELEMENTS_NUMBER
from src.handlers import normalize_input, validate_height, run_hanoi_towers_game

def main():
    print("Hello! Welcome to the Towers of Hanoi game.")

    while True:
        processed_input = normalize_input(input("Press 'q' to exit or any other key to proceed: "))

        if processed_input == "q":
            break
         
        tower_height = validate_height(input("Please, "
        "indicate the height of the tower. It can be digit "
        f"from {MIN_ELEMENTS_NUMBER} to {MAX_ELEMENTS_NUMBER}: "))

        run_hanoi_towers_game(tower_height)

if __name__ == "__main__":
    main()