import os
from dotenv import load_dotenv

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        absolute_directory = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_directory, file_path))
        
        # check if target file is within the working directory
        valid_target_dir = os.path.commonpath([absolute_directory, target_file]) == absolute_directory
        
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # Check if target file is a file
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
       
    except Exception as e:
        return f"Error: {str(e)}"
    else:
        load_dotenv()
        max_chars = int(os.environ.get("MAX_CHARS"))
        
        with open(target_file, 'r') as f:
            file_content_string = f.read(max_chars)
            
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {max_chars} characters]'
                
        return file_content_string