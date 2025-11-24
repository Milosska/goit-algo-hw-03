class PathIsNotValidException(Exception):
    def __init__(self, message="Provided path is not valid."):
        super().__init__(message)

class PathIsNotFolderException(Exception):
    def __init__(self, message="Provided path is not a path to the folder."):
        super().__init__(message)        