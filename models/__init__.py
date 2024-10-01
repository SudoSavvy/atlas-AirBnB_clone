from models.engine.file_storage import FileStorage  # Import the FileStorage class

storage = FileStorage()  # Create a single instance of the storage engine
storage.reload()  # Load existing data from the file system
