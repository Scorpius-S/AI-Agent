import os
import subprocess

def run_python_file(working_directory, file_path):
    working_directory = os.path.abspath(working_directory)
    file_path = os.path.abspath(file_path)
    if not file_path.startswith(working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_path):
        return f'Error: File "{file_path}" not found'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=working_directory
            )
        
        output = ""
        if result.stdout:
            output += f"STDOUT: {result.stdout}\n"
        if result.stderr:
            output += f"STDERR: {result.stderr}\n"
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"
        if result.stderr == "" and result.stdout == "":
            return f"No output produced."
        return output
    except subprocess.TimeoutExpired as e:
        return f"Error: executing Python file {e}"
    except Exception as e:
        return f"Error: executing Python file {e}"

        


