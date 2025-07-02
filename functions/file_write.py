import os

def write_file(working_directory, file_path, content):
    if file_path.startswith('/'):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'