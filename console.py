#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project."""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class for AirBnB clone."""

    prompt = "(hbnb) "

    def do_show(self, arg):
        """Show an instance based on its class name and id."""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                # Print the dictionary representation instead of the object memory address
                print(obj)  # You can also use print(obj.to_dict()) for a more detailed output
