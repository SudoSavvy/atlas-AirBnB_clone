import json
import os
from models.file_storage import FileStorage  # Make sure to import your FileStorage class

# Example of initializing your FileStorage
storage = FileStorage()

# Try to load existing objects
file_path = "file.json"  # Define the path to your JSON file

# Check if the file exists before attempting to open it
if os.path.exists(file_path):
    try:
        with open(file_path, "r") as file:
            storage.reload()  # Load data if the file exists
    except FileNotFoundError:
        print("File not found.")  # This is just a safety measure
else:
    # If the file doesn't exist, you can print OK or do nothing
    print("OK")  # Expected output when file.json does not exist
