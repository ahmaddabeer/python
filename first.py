import os

# Specify the directory path
directory_path = input("Enter the directory path: ")

try:
    # Get the list of all files and directories
    entries = os.listdir(directory_path)

    print(f"\nContents of '{directory_path}':")
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to access '{directory_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

