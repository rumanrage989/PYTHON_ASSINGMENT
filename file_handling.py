# file_handling_assignment.py

def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("This is the first line of text.\n")
            file.write("Here is a number: 42\n")
            file.write("This is the third line.\n")
        print("File created and written successfully.")
    except (PermissionError, IOError) as e:
        print(f"Error writing to the file: {e}")
    finally:
        print("File creation attempt complete.")

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.readlines()
            print("File content:")
            for line in content:
                print(line.strip())
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except (PermissionError, IOError) as e:
        print(f"Error reading the file: {e}")
    finally:
        print("File reading attempt complete.")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Appending a new line to the file.\n")
            file.write("Another line with a number: 99\n")
            file.write("Final line appended.\n")
        print("Content appended successfully.")
    except (PermissionError, IOError) as e:
        print(f"Error appending to the file: {e}")
    finally:
        print("File appending attempt complete.")

if _name_ == "_main_":
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read again to display the updated content