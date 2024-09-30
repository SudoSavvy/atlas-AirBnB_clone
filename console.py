#!/usr/bin/env python3
"""
Console module for the AirBnB clone project.
"""

import cmd
from models.base_model import BaseModel
from models import storage  # Make sure your storage system is correctly set up

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """End of file command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_help(self, arg):
        """Display help information for commands."""
        super().do_help(arg)

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id."""
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
        instance = storage.get(class_name, instance_id)  # Implement get method in your storage

        if instance is None:
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
        instance = storage.get(class_name, instance_id)

        if instance is None:
            print("** no instance found **")
            return

        storage.delete(class_name, instance_id)  # Implement delete method in your storage
        instance.save()  # Save changes to JSON file

    def do_all(self, arg):
        """Prints all string representation of all instances based on the class name."""
        if arg and arg != "BaseModel":
            print("** class doesn't exist **")
            return

        instances = storage.all(arg)  # Implement all method in your storage
        print([str(instance) for instance in instances.values()])

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

        if instance is None:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        value = args[3].strip('"')  # Remove quotes if any
        setattr(instance, attribute_name, value)
        instance.save()  # Save changes to JSON file

if __name__ == '__main__':
    HBNBCommand().cmdloop()
