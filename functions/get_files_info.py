import os 
import google.generativeai.types as types

def get_files_info(working_directory, directory=None):
    if directory is None:
        directory = working_directory
    
    abs_working_directory = os.path.abspath(working_directory)
    
    if not os.path.isabs(directory):
        directory = os.path.join(working_directory, directory)
    
    abs_directory = os.path.abspath(directory)
    
    if not abs_working_directory.endswith(os.sep):
        abs_working_directory += os.sep
    
    if not (abs_directory + os.sep).startswith(abs_working_directory) and abs_directory != abs_working_directory.rstrip(os.sep):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
    try:
        files = os.listdir(directory)
        result_lines = []
        
        for filename in files:
            file_path = os.path.join(directory, filename)
            is_dir = os.path.isdir(file_path)
            size = os.path.getsize(file_path)
            result_lines.append(f"- {filename}: file_size={size} bytes, is_dir={is_dir}")
        return '\n'.join(result_lines)
    except Exception as e:
        return f'Error: {str(e)}'
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)        