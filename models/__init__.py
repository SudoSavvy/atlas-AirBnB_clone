from models.engine.file_storage import FileStorage

# Create an instance of FileStorage
storage = FileStorage()

# Reload any saved data from the JSON file
storage.reload()
