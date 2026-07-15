from functions.write_file import write_file

def test_write_file():
    working_directory="calculator"
    
    file_name="lorem.txt"
    content="wait, this isn't lorem ipsum"
    print(f"Writing '{content}' to {file_name}")
    result = write_file(working_directory, file_name, content)
    print(result)
    print("-----------------------------")
    print("\n")
    
    file_name="pkg/morelorem.txt"
    content="lorem ipsum dolor sit amet"
    print(f"Writing '{content}' to {file_name}")
    result = write_file(working_directory, file_name, content)
    print(result)
    print("-----------------------------")
    print("\n")
    
    file_name="/tmp/temp.txt"
    content="this should not be allowed"
    print(f"Writing '{content}' to {file_name}")
    result = write_file(working_directory, file_name, content)
    print(result)
    print("-----------------------------")
    print("\n")
    
    
if __name__ == "__main__":
    print("Running tests for write_file")
    test_write_file()