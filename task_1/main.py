from src.handlers import parse_path, rec_copy_files
from src.decorators import handle_errors

@handle_errors
def main():
    source_path = parse_path(input("Hello! Please, enter the path to the source folder: "))
    destination_path = parse_path(input("Now enter the path to the destination folder: "), True)

    rec_copy_files(source_path, destination_path)

    print(f'Files from {source_path} are copied into {destination_path}')

if __name__ == "__main__":
    main()
