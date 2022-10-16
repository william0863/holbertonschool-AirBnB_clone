#!/usr/bin/python3
"""
contains the entry point of the command interpreter:

   ./console.py

"""

import cmd
from models import base_model
from models.engine.file_storage import FileStorage

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
            new.save()
            print (new.id)

    def do_show(self, *args):
        cmd = args[0].split()
        if (args[0] == ''):
            print ("** class name missing **")
        elif (cmd[0] not in self.models):
            print (f"** class doesn't exist **")
        elif (len(cmd) <= 1):
            print ("** instance id missing **")
        else:
            key = cmd[0] + "." + cmd[1]
            try:
                dict = FileStorage.all(self)
                print (dict[key])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, *args):
        cmd = args[0].split()
        if (args[0] == ''):
            print ("** class name missing **")
        elif (cmd[0] not in self.models):
            print (f"** class doesn't exist **")
        elif (len(cmd) <= 1):
            print ("** instance id missing **")
        else:
            key = cmd[0] + "." + cmd[1]
            try:
                dict = FileStorage.all(self)
                FileStorage.destroy(self, dict[key])
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg = None):
        if (arg != '' and arg not in self.models):
            print ("** class doesn't exist **")
        else:
            try:
                dict = FileStorage.all(self)
                for key in dict:
                    if arg == '' or key.split(".")[0] == arg:
                        print (dict[key])
            except KeyError:
                print("** no instance found **")

    def do_update(self, *args):
        cmd = args[0].split()
        if (len(cmd) <= 0 or cmd[0] == ''):
            print ("** class name missing **")
        elif (cmd[0] not in self.models):
            print (f"** class doesn't exist **")
        elif (len(cmd) <= 1 or cmd[1] == ''):
            print ("** instance id missing **")
        elif (len(cmd) <= 2 or cmd[2] == ''):
            print ("** attribute name missing **")
        elif (len(cmd) <= 3 or cmd[3] == ''):
            print ("** value missing **")
        else:
            key = cmd[0] + "." + cmd[1]
            try:
                user = FileStorage.all(self)[key]
                setattr(user, cmd[2], cmd[3])
                user.save()
            except KeyError:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
