#!/usr/bin/env python3
"""basic console program - airbnb clone"""
import cmd
import models


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
        Creates a new instance of BaseModel, saves it, and prints the id
        """
        if not args:
            print("** class name missing **")
        else:
            try:
                new_instance = models.classes[args]()
                new_instance.save()
                print(new_instance.id)
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class name and id
        """
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if args_list[0] not in models.classes:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args_list[0], args_list[1])
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if args_list[0] not in models.classes:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args_list[0], args_list[1])
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, args):
        """
        Prints all instances or all instances of a class
        """
        args_list = args.split()
        if not args:
            objects = models.storage.all()
        elif args_list[0] in models.classes:
            objects = models.storage.all(args_list[0])
        else:
            print("** class doesn't exist **")
            return

        print([str(obj) for obj in objects.values()])

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        """
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if args_list[0] not in models.classes:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args_list[0], args_list[1])
                if key not in models.storage.all():
                    print("** no instance found **")
                elif len(args_list) < 3:
                    print("** attribute name missing **")
                elif len(args_list) < 4:
                    print("** value missing **")
                else:
                    obj = models.storage.all()[key]
                    setattr(obj, args_list[2], args_list[3].strip('"'))
                    obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
