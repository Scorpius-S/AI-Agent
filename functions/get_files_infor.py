import os

def get_files_info(working_directory, directory=None):
    if directory is None:
            directory = working_directory
            if not os.path.exists(directory):
                  raise f'Error: Cannot list "{directory}" as it is outside the permitted working directory'