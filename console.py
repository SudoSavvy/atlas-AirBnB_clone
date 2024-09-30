import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB AirBnB clone."""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        
        instance = BaseModel()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        instance_id = args[1]
        instance = storage.get(class_name, instance_id)
        if not instance:
            print("** no instance found **")
            return
        
        print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        instance_id = args[1]
        if storage.destroy(class_name, instance_id):
            print(f"Instance {instance_id} destroyed.")
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances, or instances of a specific class."""
        if arg and arg != "BaseModel":
            print("** class doesn't exist **")
            return
        
        instances = storage.all(arg)
        print([str(instance) for instance in instances])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating an attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        instance_id = args[1]
        instance = storage.get(class_name, instance_id)
        if not instance:
            print("** no instance found **")
            return
        
        if len(args) < 3:
            print("** attribute name missing **")
            return
        
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        
        attribute_value = arg.split(' ', 3)[3].strip('"')
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_quit(self, arg):
        """Exits the command interpreter."""
        sys.exit()

    def do_EOF(self, arg):
        """Handles the End Of File (CTRL+D) to exit the interpreter."""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
