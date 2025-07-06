import os

def run_python_file(working_directory, file_path):
    working_directory = os.path.abspath(working_directory)
    file_path = os.path.abspath(file_path)
    if not file_path.startswith(working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
