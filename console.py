#!/usr/bin/python3
"""This module defines the console for the AirBnB clone project."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This class defines the command line interpreter."""

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]  # Extract class name
        if class_name not in [
                "BaseModel", "User", "State", "City", "Amenity", "Place",
                "Review"]:
            print("** class doesn't exist **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** failed to create instance **")

    def do_show(self, arg):
        """Show the string representation of an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel", "User", "State", "City",
                             "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            print(objects[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel", "User", "State", "City",
                             "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            del objects[key]
            storage.save()

    def do_all(self, arg):
        """Print all string representations of all instances."""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return
        class_name = arg.split('(')[0]
        if class_name not in [
                "BaseModel", "User", "State", "City", "Amenity", "Place",
                "Review"]:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in objects.items() if key.startswith(
            class_name + ".")])

    def do_count(self, arg):
        """Count the instances of a class."""
        if not arg:
            print("** class name missing **")
            return
        try:
            obj_class = eval(arg)
        except NameError:
            print("** class doesn't exist **")
            return
        objects = storage.all()
        args = arg.split()
        count = sum([1 for key in objects.keys() if args[0] in key])
        print(count)

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel", "User", "State", "City",
                             "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(objects[key], args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
