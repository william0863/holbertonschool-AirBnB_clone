#!/usr/bin/python3
"""
Unittest for BaseModel class
"""

import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    """
    Test cases for base_model class
    """

        def test_save(self):
            self.base1.save()
            self.assertNotEqual(self.base1.created_at, self.base1.updated_at)


