#!/usr/bin/python3
"""Module that sets up the models package."""
from models import storage  # Ensure the storage engine is imported correctly

# Create a unique FileStorage instance for the project
storage = FileStorage()

# Call reload to load storage data from the JSON file
storage.reload()
