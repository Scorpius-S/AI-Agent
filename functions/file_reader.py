import os

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    combined_path = os.path.join(abs_working_directory, file_path)
    if not combined_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(combined_path):
        return f'Error: File not found or is not a regular file: {file_path}'
    file_content = read_with_truncation(combined_path)
    return file_content
    
def read_with_truncation(combined_path, max_chars=10000):
    abs_path = os.path.abspath(combined_path)
    content = ""
    try:
        with open(abs_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read(max_chars)
            overflow = f.read(1)
            if overflow:
                content += (
                    f"\n\n"
                    f"[...File \"{combined_path}\" truncated at {max_chars} characters]"
                )
        return content
    except IOError as e:
        return f"Error: Failed to read file \"{combined_path}\" due to {str(e)}"