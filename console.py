#!/usr/bin/python3
"""
contains the entry point of the command interpreter:

   ./console.py

"""

import cmd
from models import base_model

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None
    models = ("BaseModel", "User")

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

    def do_create(self, arg = None):
        if (arg == ''):
            print ("** class name missing **")
        elif (arg not in self.models):
            print ("** class doesn't exist **")
        else:
            new = eval("base_model." + arg)()
            print (new.id)

    def do_show(self, *args):
        if (args[0] == ''):
            print ("** class name missing **")
        elif (args[0] not in self.models):
            print ("** class doesn't exist **")
        elif (len(args) <= 1):
            print ("** instance id missing **")
        else:
            new = args()
            print (type(new))

    def do_destroy(self, *args):
        if (args[0] == ''):
            print ("** class name missing **")
        elif (args[0] not in self.models):
            print ("** class doesn't exist **")
        elif (len(args) <= 1):
            print ("** instance id missing **")
        else:
            new = args()
            print (type(new))



if __name__ == '__main__':
    HBNBCommand().cmdloop()

