import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True
    
    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)."""
        return True
    
    def do_help(self, arg):
        """Override the help command to include custom commands."""
        super().do_help(arg)

        def emptyline(self):
            """Do nothing on empty line + ENTER."""
            pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()