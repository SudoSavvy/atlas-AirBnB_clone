import cmd
from models.file_storage import FileStorage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone."""

    prompt = '(hbnb) '
    storage = FileStorage()

    def do_create(self, class_name):
        """Creates a new instance of BaseModel."""
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in ["BaseModel"]:  # Add other valid classes as needed
            print("** class doesn't exist **")
            return
        instance = eval(class_name)()  # Create a new instance of the class
        instance.save()  # Save the instance
        print(instance.id)  # Print the id of the created instance

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel"]:  # Add other valid classes as needed
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in self.storage.all():
            print("** no instance found **")
            return
        print(self.storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel"]:  # Add other valid classes as needed
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in self.storage.all():
            print("** no instance found **")
            return
        del self.storage.all()[key]
        self.storage.save()

    def do_all(self, class_name=None):
        """Prints all string representation of all instances."""
        if class_name and class_name not in ["BaseModel"]:  # Add other valid classes as needed
            print("** class doesn't exist **")
            return
        all_instances = self.storage.all()
        if class_name:
            instances = [str(v) for k, v in all_instances.items() if k.startswith(class_name)]
        else:
            instances = [str(v) for v in all_instances.values()]
        print(instances)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel"]:  # Add other valid classes as needed
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in self.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        value = args[3].strip('"')  # Remove quotes
        instance = self.storage.all()[key]
        setattr(instance, attribute_name, value)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
