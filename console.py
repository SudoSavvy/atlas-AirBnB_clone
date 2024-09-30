import cmd
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone."""

    prompt = '(hbnb) '

    def do_create(self, line):
        """Creates a new instance of a class."""
        if not line:
            print("** class name missing **")
            return

        class_name = line.split()[0]
        if class_name not in [
            "BaseModel", "Place", "State", "City", "Amenity", "Review"
        ]:
            print("** class doesn't exist **")
            return

        obj = eval(f"{class_name}()")
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """Shows an instance of a class based on class name and id."""
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, obj_id = args
        if class_name not in [
            "BaseModel", "Place", "State", "City", "Amenity", "Review"
        ]:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{obj_id}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return

        print(obj)

    def do_destroy(self, line):
        """Destroys an instance based on class name and id."""
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, obj_id = args
        if class_name not in [
            "BaseModel", "Place", "State", "City", "Amenity", "Review"
        ]:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{obj_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, line):
        """Updates an instance based on class name and id by adding or updating attribute."""
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if len(args) < 3:
            print("** instance id missing **")
            return

        if len(args) < 4:
            print("** attribute name missing **")
            return

        if len(args) < 5:
            print("** value missing **")
            return

        class_name, obj_id, attr_name, attr_value = args[0], args[1], args[2], args[3]
        if class_name not in [
            "BaseModel", "Place", "State", "City", "Amenity", "Review"
        ]:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{obj_id}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return

        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_quit(self, line):
        """Exits the command interpreter."""
        return True

    def do_EOF(self, line):
        """Handles end of file."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
