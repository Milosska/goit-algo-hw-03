## Task 1

Write a Python program that recursively copies files from a source directory, moves them to a new destination directory, and sorts them into subdirectories named after their file extensions.

### Requirements

1. Argument parsing: The script should accept two command-line arguments: the path to the source directory and the path to the destination directory. If the destination directory is not provided, it should default to a folder named dist.
2. Recursive directory reading:

   - Implement a function that takes a directory path as an argument.
   - The function should iterate over all items in the directory.
   - If an item is a directory, the function should call itself recursively on that directory.
   - If an item is a file, it should be processed for copying.

3. File copying:
   For each file type, create a corresponding folder in the destination directory using the file extension as the folder name.Copy each file into its corresponding extension-based subdirectory.
4. Exception handling: The code should handle exceptions, such as file or directory access errors.
5. Outcome: After running the program, all files from the source directory should be recursively copied to the destination directory and sorted into subdirectories based on their extensions.
