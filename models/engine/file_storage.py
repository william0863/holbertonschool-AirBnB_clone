#!/usr/bin/python3
"""The class FileStorage"""

from models.base_model import BaseModel
import json
from datetime import datetime


class FileStorage:
    """Represents the class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in objects"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        new_dict = {}

        for key, obj in self.__objects.items():
            '''if type(obj) is dict:
            my_dict[key] = obj
            else:'''
            new_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
           with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
