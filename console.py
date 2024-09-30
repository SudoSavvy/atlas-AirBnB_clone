#!/usr/bin/env python3
"""
Console module for the AirBnB clone project.
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone."""

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            instance = self.classes[arg]()
            instance.save()  # Save the instance to the file
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            instance = storage.all().get(key)
            if instance is None:
                print("** no instance found **")
            else:
                print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()  # Save after deletion

    def do_all(self, arg):
        """Prints all string representations of all instances, or instances of a class."""
        if not arg:
            objects = [str(v) for v in storage.all().values()]
            print(objects)
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            objects = [str(v) for k, v in storage.all().items() if k.startswith(arg)]
            print(objects)

    def do_update(self, arg):
        """Updates an instance by adding or updating attributes."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            instance = storage.all().get(key)
            if instance is None:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                attr_name = args[2]
                attr_value = args[3].strip('"')
                setattr(instance, attr_name, attr_value)
                instance.save()  # Save updated instance

    def emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """End of file command to exit the program."""
        return True

    def do_help(self, arg):
        """Display help information for commands."""
        super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
