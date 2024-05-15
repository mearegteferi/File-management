import os
import shutil
import hashlib

class FileManager:
    def __init__(self):
        self.current_directory = os.getcwd()
    def change_directory(self, path):
        """
        Change the current working directory to the specified path.

        Args:
        path (str): The path to change the directory to.
        """
        if not path:
            raise OSError("Path cannot be empty")
        elif os.path.isdir(path):
            self.current_directory = path
        else:
            raise OSError(f"{path} is not a valid directory.")
        
    def read_file(self, file_path):
        """
        Read the content of the specified file.

        Args:
            file_path (str): The path of the file to read.

        Returns:
            str: The content of the file.
        """
        
        with open(file_path, 'r') as f:
                return f.read()