#!/usr/bin/python3
import cmd
from models.engine import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB console."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program with EOF (Ctrl+D).

        Usage: EOF
        """
        print("")
        return True

    def do_show(self, arg):
        """
        Print the string representation of an instance.

        Usage: show <class_name> <instance_id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print all string representations of all instances.

        Usage: all [<class_name>]
        """
        args = arg.split()
        objs = []
        if not arg:
            for obj in storage.all().values():
                objs.append(str(obj))
            print(objs)
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        for key, obj in storage.all().items():
            if key.split('.')[0] == args[0]:
                objs.append(str(obj))
        print(objs)

    def do_update(self, arg):
        """
        Update an instance based on the class name and id.

        Usage: update <class_name> <instance_id>
        <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(storage.all()[key], args[2], args[3])
        storage.all()[key].save()

    def do_create(self, arg):
        """
        Create a new instance of BaseModel,
        save it to JSON file and print its id.

        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(arg)
        except NameError:
            print("** class doesn't exist **")
            return
        obj = cls()
        obj.save()
        print(obj.id)

    def do_destroy(self, arg):
        """
        Destroy an instance based on its ID.

        Usage: <class_name>.destroy(<id>)
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_count(self, arg):
        """
        Count instances of a class.

        Usage: <class_name>.count()
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        count = sum
        (1 for obj in storage.all().values() if isinstance(obj, cls))
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
