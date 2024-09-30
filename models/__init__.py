#!/usr/bin/python3
"""Module that sets up the models package."""
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for the project
storage = FileStorage()

# Call reload to load storage data from the JSON file
storage.reload()
