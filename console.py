"""
Console module for the AirBnB clone project.
"""

import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
