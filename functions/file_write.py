import os

def write_file(working_directory, file_path, content):
    absolute_path = os.path.abspath(file_path)
    absolute_working_directory = os.path.abspath(working_directory)
    final_target_absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
    common_dir = os.path.commonpath([final_target_absolute_path, absolute_working_directory])
    if common_dir != absolute_working_directory:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    os.makedirs(os.path.dirname(final_target_absolute_path), exist_ok=True)
    with open(final_target_absolute_path, 'w') as file:
        file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
