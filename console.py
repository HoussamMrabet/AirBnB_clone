#!/usr/bin/env python3
"""basic console program - airbnb clone"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        Exit the program on EOF (Ctrl+D)
        """
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """
        Do nothing on an empty line
        """
        pass

    def do_create(self, args):
        """
        Create a new instance of BaseModel, save it, and print the id
        """
        if not args:
            print("** class name missing **")
            return

        try:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(e)

    def do_show(self, args):
        """
        Print the string representation of an instance
        """
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        if args_list[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        obj_key = args_list[0] + "." + args_list[1]
        obj_dict = storage.all()
        if obj_key not in obj_dict.keys():
            print("** no instance found **")
            return

        print(obj_dict[obj_key])

    def do_destroy(self, args):
        """
        Destroy an instance based on the class name and id
        """
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        if args_list[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        obj_key = args_list[0] + "." + args_list[1]
        obj_dict = storage.all()
        if obj_key not in obj_dict.keys():
            print("** no instance found **")
            return

        del obj_dict[obj_key]
        storage.save()

    def do_all(self, args):
        """
        Print string representation of all instances based on class name
        """
        args_list = args.split()
        obj_list = []
        if args_list and args_list[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return

        obj_dict = storage.all()
        for obj_key in obj_dict.keys():
            if not args_list or obj_key.split(".")[0] == args_list[0]:
                obj_list.append(str(obj_dict[obj_key]))
        print(obj_list)

    def do_update(self, args):
        """
        Update an instance attribute based on class name and id
        """
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        if args_list[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        obj_key = args_list[0] + "." + args_list[1]
        obj_dict = storage.all()
        if obj_key not in obj_dict.keys():
            print("** no instance found **")
            return

        if len(args_list) < 3:
            print("** attribute name missing **")
            return

        if len(args_list) < 4:
            print("** value missing **")
            return

        attr_name = args_list[2]
        attr_value = args_list[3]

        # Handle attribute type casting based on the model's attributes
        if hasattr(obj_dict[obj_key], attr_name):
            attr_type = type(getattr(obj_dict[obj_key], attr_name))
            try:
                casted_value = attr_type(attr_value)
                setattr(obj_dict[obj_key], attr_name, casted_value)
                obj_dict[obj_key].save()
            except ValueError:
                print("** invalid value **")

    def do_BaseModel(self, args):
        """
        Handle BaseModel class specific commands
        """
        if args == ".all()":
            self.do_all("BaseModel")
        elif args.startswith(".show("):
            self.do_show("BaseModel " + args[7:-1])
        elif args.startswith(".destroy("):
            self.do_destroy("BaseModel " + args[10:-1])
        elif args.startswith(".update("):
            update_args = args[9:-1].split(", ")
            if len(update_args) >= 2:
                self.do_update("BaseModel " + update_args[0] + " " + update_args[1])
            if len(update_args) >= 3:
                self.do_update(
                    "BaseModel "
                    + update_args[0]
                    + " "
                    + update_args[1]
                    + " "
                    + update_args[2]
                )
        else:
            print("*** Unknown syntax: BaseModel" + args)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
