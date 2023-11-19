# read a file

### entire content
    # Open a file in read mode
    file_path = 'path/to/your/file.txt'  # Replace with the actual file path
    try:
        with open(file_path, 'r') as file:
            # Read the entire file content
            content = file.read()
            print(content)
            
    except FileNotFoundError:
        print("The file does not exist or the path is incorrect.")
    except IOError:
        print("An error occurred while reading the file.")

### line by line
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line)

    except FileNotFoundError:
        print("The file does not exist or the path is incorrect.")

    except IOError:
        print("An error occurred while reading the file.")


# all operations

import os
 
    def create_file(filename):
        try:
            with open(filename, 'w') as f:
                f.write('Hello, world!\n')
            print("File " + filename + " created successfully.")
        except IOError:
            print("Error: could not create file " + filename)
    
    def read_file(filename):
        try:
            with open(filename, 'r') as f:
                contents = f.read()
                print(contents)
        except IOError:
            print("Error: could not read file " + filename)
    
    def append_file(filename, text):
        try:
            with open(filename, 'a') as f:
                f.write(text)
            print("Text appended to file " + filename + " successfully.")
        except IOError:
            print("Error: could not append to file " + filename)
    
    def rename_file(filename, new_filename):
        try:
            os.rename(filename, new_filename)
            print("File " + filename + " renamed to " + new_filename + " successfully.")
        except IOError:
            print("Error: could not rename file " + filename)
    
    def delete_file(filename):
        try:
            os.remove(filename)
            print("File " + filename + " deleted successfully.")
        except IOError:
            print("Error: could not delete file " + filename)
 