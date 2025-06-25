import os #Importing os module to interact with the operating system

def get_files_info(working_directory, directory=None):
    if directory is None:
        directory = working_directory
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(directory)

    if not abs_directory.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
            