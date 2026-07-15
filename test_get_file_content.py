
from functions.get_file_content import get_file_content

def test_get_file_content():
    working_directory="calculator"
    
    file_test="lorem.txt"
    result = get_file_content(working_directory, file_test)
    print(f"Result for '{file_test}':")
    print(f"{file_test} length: {len(result)}")
    print(f"{file_test} truncated: {'truncated' in result}")
    print("\n")
    
    file_test="main.py"
    result = get_file_content(working_directory, file_test)
    print(f"Result for '{file_test}':")
    print(result)
    print("\n")
    
    file_test="pkg/calculator.py"
    result = get_file_content(working_directory, file_test)
    print(f"Result for '{file_test}':")
    print(result)
    print("\n")
    
    file_test="/bin/cat"
    result = get_file_content(working_directory, file_test)
    print(f"Result for '{file_test}':")
    print(result)
    print("\n")
    
    file_test="pkg/does_not_exist.py"
    result = get_file_content(working_directory, file_test)
    print(f"Result for '{file_test}':")
    print(result)
    print("\n")
    
    
if __name__ == "__main__":
    print("Running test for get_file_content...")
    test_get_file_content()