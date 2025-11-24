from functools import wraps
from typing import Callable

def handle_errors(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)

        except Exception as error:
            print(error)
            return

    return wrapper         