import cmd  # Importing the cmd module to create command-line interpreters
from models import storage  # Importing the storage module for data persistence
from models.place import Place  # Importing the Place class
from models.state import State  # Importing the State class
from models.city import City  # Importing the City class
from models.amenity import Amenity  # Importing the Amenity class
from models.review import Review  # Importing the Review class

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone."""  # Documentation for the class

    prompt = '(hbnb) '  # Setting the command prompt

    def do_create(self, line):
        """Creates a new instance of a class."""  # Documentation for the create command
        if not line:  # Check if the line is empty
            print("** class name missing **")  # Error message for missing class name
            return  # Exit the function

        class_name = line.split()[0]  # Extracting the class name from the input line
        if class_name not in [
            "BaseModel", "Place", "State", "City", "Amenity", "Review"
        ]:  # Validating the class name
            print("** class doesn't exist **")  # Error message for invalid class name
            return  # Exit the function

        obj = eval(f"{class_name}()")  # Dynamically creating an instance of the class
        obj.save()  # Saving the instance
        print(obj.id)  # Printing the ID of the created instance

    def do_show(self, line):
        """Shows an instance of a class based on class name and id."""  # Documentation for the show command
        if not line:  # Check if the line is empty
            print("** class name missing **")  # Error message for missing class name
            return  # Exit the function

        args = line.split()  # Splitting the input line into arguments
        if len(args) < 2:  # Check if instance ID is provided
            print("** instance id missing **")  # Error message for missing instance ID
            return  # Exit the function

        class_name, obj_id = args  # Unpacking the class name and instance ID
        if class_name not in [
            "BaseModel", "Place", "State", "City", "Amenity", "Review"
        ]:  # Validating the class name
            print("** class doesn't exist **")  # Error message for invalid class name
            return  # Exit the function

        key = f"{class_name}.{obj_id}"  # Creating the key for storage
        obj = storage.all().get(key)  # Retrieving the object from storage
        if not obj:  # Check if the object exists
            print("** no instance found **")  # Error message for missing instance
            return  # Exit the function

        print(obj)  # Printing the object

    def do_destroy(self, line):
        """Destroys an instance based on class name and id."""  # Documentation for the destroy command
        if not line:  # Check if the line is empty
            print("** class name missing **")  # Error message for missing class name
            return  # Exit the function

        args = line.split()  # Splitting the input line into arguments
        if len(args) < 2:  # Check if instance ID is provided
            print("** instance id missing **")  # Error message for missing instance ID
            return  # Exit the function

        class_name, obj_id = args  # Unpacking the class name and instance ID
        if class_name not in [
            "BaseModel", "Place", "State", "City", "Amenity", "Review"
        ]:  # Validating the class name
            print("** class doesn't exist **")  # Error message for invalid class name
            return  # Exit the function

        key = f"{class_name}.{obj_id}"  # Creating the key for storage
        if key in storage.all():  # Check if the object exists in storage
            del storage.all()[key]  # Deleting the object from storage
            storage.save()  # Saving the changes
        else:
            print("** no instance found **")  # Error message for missing instance

    def do_update(self, line):
        """Updates an instance based on class name and id by adding or updating attribute."""  # Documentation for the update command
        if not line:  # Check if the line is empty
            print("** class name missing **")  # Error message for missing class name
            return  # Exit the function

        args = line.split()  # Splitting the input line into arguments
        if len(args) < 3:  # Check if instance ID is provided
            print("** instance id missing **")  # Error message for missing instance ID
            return  # Exit the function

        if len(args) < 4:  # Check if attribute name is provided
            print("** attribute name missing **")  # Error message for missing attribute name
            return  # Exit the function

        if len(args) < 5:  # Check if value is provided
            print("** value missing **")  # Error message for missing value
            return  # Exit the function

        class_name = args[0]  # Extracting the class name
        obj_id = args[1]  # Extracting the instance ID
        attr_name = args[2]  # Extracting the attribute name
        attr_value = args[3]  # Extracting the attribute value

        if class_name not in [
            "BaseModel", "Place", "State", "City", "Amenity", "Review"
        ]:  # Validating the class name
            print("** class doesn't exist **")  # Error message for invalid class name
            return  # Exit the function

        key = f"{class_name}.{obj_id}"  # Creating the key for storage
        obj = storage.all().get(key)  # Retrieving the object from storage
        if not obj:  # Check if the object exists
            print("** no instance found **")  # Error message for missing instance
            return  # Exit the function

        setattr(obj, attr_name, attr_value)  # Setting the attribute value on the object
        obj.save()  # Saving the changes

    def do_quit(self, line):
        """Exits the command interpreter."""  # Documentation for the quit command
        return True  # Returning True to exit the command loop

    def do_EOF(self, line):
        """Handles end of file."""  # Documentation for EOF command
        return True  # Returning True to exit the command loop

if __name__ == '__main__':
    HBNBCommand().cmdloop()  # Starting the command interpreter loop
