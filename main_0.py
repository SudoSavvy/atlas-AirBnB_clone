from models.file_storage import FileStorage
from models.base_model import BaseModel

# Create a global storage instance
storage = FileStorage()
storage.reload()  # Load existing data from the JSON file

# Create an instance of your console
my_console = MyConsole()  # Replace with your console class name
