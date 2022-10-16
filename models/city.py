#!/usr/bin/python3
"""
contains the City class

"""


from models.base_model import BaseModel

class City(BaseModel):
    """

    city has the following attributes:
        name: the name of the city
        state_id: the id of the affiliated state

    """

    name = ""
    state_id = ""

