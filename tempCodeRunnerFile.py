def do_update(self, line):
    """Updates an instance based on class name and id by adding or updating attribute."""
    if not line:  # Check if the line is empty
        print("** class name missing **")  # Error message for missing class name
        return  # Exit the function

    args = line.split()  # Splitting the input line into arguments
    if len(args) < 2:  # Check if instance ID is provided
        print("** instance id missing **")  # Error message for missing instance ID
        return  # Exit the function

    if len(args) < 3:  # Check if attribute name is provided
        print("** attribute name missing **")  # Error message for missing attribute name
        return  # Exit the function

    if len(args) < 4:  # Check if value is provided
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
