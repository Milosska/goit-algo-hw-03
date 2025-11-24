import shutil
from pathlib import Path
from src.exceptions import PathIsNotValidException, PathIsNotFolderException

def parse_path(input_str: str | None, is_default = False) -> Path:
    if input_str is None or input_str.strip() == "":
        if is_default:
            source_path = Path('./dist')
            source_path.mkdir(parents=True, exist_ok=True)
            return source_path
        else:
           raise PathIsNotValidException() 

    source_path = Path(input_str.replace("\"", ""))
    if not source_path.exists():
        raise PathIsNotValidException()
    
    if not source_path.is_dir():
        raise PathIsNotFolderException()
    
    return source_path

def rec_copy_files(source_path: Path, destination_path: Path) -> None:
    for inner_path in source_path.iterdir():
        if inner_path.is_dir():
            rec_copy_files(inner_path, destination_path)
            continue

        target_path = Path(f'{destination_path}/{inner_path.suffix[1::]}')
        if not target_path.exists():
            target_path.mkdir(parents=True, exist_ok=False)
        
        shutil.copy2(inner_path, target_path)
    