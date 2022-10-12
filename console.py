#!/usr/bin/python3
"""
contains the entry point of the command interpreter:

   ./console.py

"""

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None

    def emptyline(arg):
        pass

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        if arg == '':
            return 1

    def do_quit(self, arg):
        """Quit command to exit the program"""
        if arg == '':
            return 1

if __name__ == '__main__':
    HBNBCommand().cmdloop()

