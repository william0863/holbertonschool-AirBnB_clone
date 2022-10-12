#!/usr/bin/python3
"""
module "base_model"
"""

from uuid import uuid4
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
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
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

    def __repr__(self):
        """
        returns string representation
        """
        return (self.__str__())

    def to_dict(self):
        """
        Return dict with string formats of time & add class info to dict
        """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic
