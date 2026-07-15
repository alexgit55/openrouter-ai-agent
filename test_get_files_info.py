import os
from functions.get_files_info import get_files_info

def test_get_files_info():
    working_directory = os.getcwd()  # Get the current working directory

    # Test case 1: Valid directory within the working directory
    result = get_files_info('calculator', ".")
    print(f"Result for current directory: ")
    print(result)

    # Test case 2: Valid subdirectory within the working directory
    result = get_files_info('calculator', "pkg") 
    print(f"Result for 'pkg' directory: ")
    print(result)

    # Test case 3: Invalid directory outside the working directory
    result = get_files_info('calculator', "/bin") 
    print(f"Result for '/bin' directory: ")
    print(result)

    # Test case 4: Non-directory file path (should return an error)
    result = get_files_info('calculator', "../")
    print(f"Result for '../' directory: ")
    print(result)
    
if __name__ == "__main__":
    print("Running tests for get_files_info...")
    test_get_files_info()