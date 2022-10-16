#!/usr/bin/python3
"""
contains the user class

"""


from models.base_model import BaseModel


class User(BaseModel):
    """ User has the following attributes:
    email (string): the email of the user
    password (string): the password of the user
    first_name (string): the first name of the user
    last_name (string): the last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
