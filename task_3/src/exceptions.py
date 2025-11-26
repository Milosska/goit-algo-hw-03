from src.constants import MIN_ELEMENTS_NUMBER, MAX_ELEMENTS_NUMBER

class ValueIsNotValidException(Exception):
    def __init__(self, message=("Tower height is not valid. "
                 f"Please, enter any digit between {MIN_ELEMENTS_NUMBER} and {MAX_ELEMENTS_NUMBER}.")):
        super().__init__(message)           