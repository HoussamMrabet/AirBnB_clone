#!/usr/bin/python3
import cmd

class hbnb(cmd.Cmd):
    prompt = '(hbnb) '
        
    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_quit(self, arg):
        """Exit the application"""
        return True
    
    def do_EOF(self, arg):
        """get the end of file"""
        print("")
        return True

if __name__ == '__main__':
    hbnb().cmdloop()
