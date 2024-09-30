# AirBnB Clone

## Description

The AirBnB Clone is a command-line interpreter designed to manage AirBnB objects, enabling users to create, retrieve, update, and delete objects for rental properties. This project is an essential part of the Holberton School curriculum and serves as a foundational learning experience in Python programming, object-oriented design, and application development.

## Command Interpreter

The command interpreter allows users to interact with the AirBnB clone through the terminal, executing commands to manipulate various objects within the application.

### How to Start It

To start the command interpreter, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/SudoSavvy/atlas-AirBnB_clone.git
   ```

2. Navigate to the project directory:

   ```bash
   cd atlas-AirBnB_clone
   ```

3. Run the command interpreter:

   ```bash
   python3 console.py
   ```

### How to Use It

Once you start the interpreter, you can enter various commands to interact with the application. Here are some of the available commands:

- `create <class>`: Creates a new instance of the specified class and saves it to a JSON file.
- `show <class> <id>`: Displays the string representation of an instance based on its class name and id.
- `destroy <class> <id>`: Deletes an instance based on the class name and id.
- `all <class>`: Displays all instances of a specified class, or all instances if no class is specified.
- `update <class> <id> <attribute> <value>`: Updates an instance based on class name and id with new attribute values.

### Examples

Here are some examples of how to use the command interpreter:

- Create a new User instance:

  ```bash
  create User
  ```

- Show the details of a User instance with a specific ID:

  ```bash
  show User <user_id>
  ```

- Update an attribute of the User instance:

  ```bash
  update User <user_id> name "John Doe"
  ```

- List all instances of the User class:

  ```bash
  all User
  ```

- Delete a User instance:

  ```bash
  destroy User <user_id>
  ```

For more details, refer to the project documentation.