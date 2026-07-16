from functions.run_python_file import run_python_file

def test_run_python_file():
    working_directory="calculator"
    
    file_name="main.py"
    args=[]
    print(f"Running '{file_name}'")
    result = run_python_file(working_directory, file_name, args)
    print(result)
    print("-----------------------------")
    print("\n")
    
    file_name="main.py"
    args=["3 + 5"]
    print(f"Running '{file_name}'")
    result = run_python_file(working_directory, file_name, args)
    print(result)
    print("-----------------------------")
    print("\n")
    
    file_name="tests.py"
    args=[]
    print(f"Running '{file_name}'")
    result = run_python_file(working_directory, file_name, args)
    print(result)
    print("-----------------------------")
    print("\n")
    
    file_name="../main.py"
    args=[]
    print(f"Running '{file_name}'")
    result = run_python_file(working_directory, file_name, args)
    print(result)
    print("-----------------------------")
    print("\n")
    
    file_name="nonexistent.py"
    args=[]
    print(f"Running '{file_name}'")
    result = run_python_file(working_directory, file_name, args)
    print(result)
    print("-----------------------------")
    print("\n")
    
    file_name="lorem.txt"
    args=[]
    print(f"Running '{file_name}'")
    result = run_python_file(working_directory, file_name, args)
    print(result)
    print("-----------------------------")
    print("\n")
    
    


if __name__ == "__main__":
    print("Running tests for run_python_file")
    test_run_python_file()