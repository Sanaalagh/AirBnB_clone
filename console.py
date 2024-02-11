#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
# from models.base_model import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    'BaseModel': BaseModel,
    # 'User': User,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review
}

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
        objs = storage.all()
        if len(args) < 1:
            print(["{}".format(v) for _, v in objs.items()])
            return
        if args[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        else:
            print(["{}".format(v) for _, v in objs.items()])

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
        create new instance
        """
        args = arg.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes.keys():
            print("** class doesn't exist **")
        else:
            new_instance = classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

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
