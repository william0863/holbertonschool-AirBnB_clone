#!/usr/bin/python3
"""The class FileStorage"""

from models import base_model
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
import json
from datetime import datetime
import os

class FileStorage:
    """Represents the class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in objects"""
        if obj:
            key = f'{obj.__class__.__name__}.{obj.id}'
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        new_dict = {}

        for key, obj in FileStorage.__objects.items():
            '''if type(obj) is dict:
            my_dict[key] = obj
            else:'''
            new_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                a = f.read()
                new_obj = json.loads(a)
            for key, val in new_obj.items():
                if type(val) is dict:
                    FileStorage.__objects[key] = eval(val['__class__'])(**val)
        except FileNotFoundError:
            pass

    def destroy(self, obj):
        """deletes an object forme a save"""
        if obj:
            key = f'{obj.__class__.__name__}.{obj.id}'
            del FileStorage.__objects[key]
