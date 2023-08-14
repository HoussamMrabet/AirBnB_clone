#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, command):
        exit()

    def help_quit(self):
        print("Exits the program with formatting")

    def do_EOF(self, arg):
        exit()

    def help_EOF(self):
        print("Exits the program without formatting")

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
