#!/usr/bin/python3
"""
module "base_model"
"""

import os
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base class for Airbnb clone project
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes
        """
        if kwargs:
            for key, val in kwargs.items():
                if 'created_at' == key:
                    self.created_at= datetime.strptime(kwargs['created_at'],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif 'updated_at' == key:
                    self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return string info about model
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        updates "updated_at" instance with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dict with string formats of time & add class info to dict
        """
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        new_dict['__class__'] = type(self).__name__
        return new_dict
