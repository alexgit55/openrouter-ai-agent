import os
from pathlib import Path

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes text content to a specified file within the working directory (overwriting if the file exists)",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Text content to write to the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        absolute_directory = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_directory, file_path))
        
        # check if target file is within the working directory
        valid_target_dir = os.path.commonpath([absolute_directory, target_file]) == absolute_directory
        
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # Check if target file is a file
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
       
    except Exception as e:
        return f"Error: {str(e)}"
    else:
        parent_directory=Path(target_file).parent
        Path(parent_directory).mkdir(parents=True, exist_ok=True)
        with open(target_file, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'