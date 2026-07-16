from pathlib import Path
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified Python file within the working directory and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to run, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of arguments to pass to the Python script",
                },
            },
            "required": ["file_path"],
        },
    },
}

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        absolute_directory = Path(working_directory).resolve()
        target_file = (absolute_directory / file_path).resolve()
        
        # check if target file is within the working directory
        valid_target_dir = (
            target_file == absolute_directory
            or absolute_directory in target_file.parents
        )
        
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # Check if target file is a file
        if not target_file.is_file():
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        #Check if target file is a python file
        if not target_file.suffix == '.py':
            return f'Error: "{file_path}" is not a Python file'
            
    except Exception as e:
        return f"Error: {str(e)}"
    else:
        command = ["python3", target_file]
        if args:
            command.extend(args)
        try:
            completed_process = subprocess.run(command, 
                                               capture_output=True, 
                                               text=True,
                                               timeout=30)
        except Exception as e:
            return f"Error: executing Python file: {str(e)}"
        else:
            output_string=[]
            if completed_process.returncode != 0:
                output_string.append(f"Process exited with code {completed_process.returncode}")
                
            if not completed_process.stderr and not completed_process.stdout:
                output_string.append("No Output produced")
            elif completed_process.stderr:
                output_string.append(f"STDERR: {completed_process.stderr}")
            elif completed_process.stdout:
                output_string.append(f"STDOUT: {completed_process.stdout}")
                
            return "\n".join(output_string)
                