import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_files_info(working_directory: str, directory: str = ".") -> str:
 
    try:
        absolute_directory = os.path.abspath(working_directory)
        target_directory = os.path.normpath(os.path.join(absolute_directory, directory))
        
        # check if target directory is a valid directory
        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'
        
        # check if target directory is within the working directory
        valid_target_dir = os.path.commonpath([absolute_directory, target_directory]) == absolute_directory
        
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except Exception as e:
        return f"Error: {str(e)}"
    else:
        files = os.listdir(target_directory)
        files_info = []
        for file in files:
            file_name=file
            file_size=os.path.getsize(os.path.join(target_directory, file))
            is_directory=os.path.isdir(os.path.join(target_directory, file))
            file_info=f"- {file_name}: file_size={file_size} bytes, is_dir={is_directory}"
            files_info.append(file_info)
        return "\n".join(files_info)
        
            