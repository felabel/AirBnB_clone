#!/usr/bin/pyton3
"""Defines unittests for models/amenity.py"""

import os
import unittest
from models.amenity import Amenity
from datetime import datetime
from time import sleep
import models


class TestAmenity(unittest.TestCase):
    """Test case for Amenity class."""

    def test_init(self):
        """Test Amenity initialization."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertEqual(amenity.name, "")

        # Test initialization with kwargs
        kwargs = {'id': 'test_id', 'created_at': '2022-02-13T12:00:00.000000',
                  'updated_at': '2022-02-13T12:00:00.000000', 'name': 'test_name'}
        amenity_with_kwargs = Amenity(**kwargs)
        self.assertEqual(amenity_with_kwargs.id, 'test_id')
        self.assertEqual(amenity_with_kwargs.created_at, datetime(2022, 2, 13, 12, 0))
        self.assertEqual(amenity_with_kwargs.updated_at, datetime(2022, 2, 13, 12, 0))
        self.assertEqual(amenity_with_kwargs.name, 'test_name')

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, models.base_model.BaseModel)

    def test_to_dict(self):
        """Test to_dict method."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('__class__', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIn('id', amenity_dict)
        self.assertEqual(amenity_dict['id'], amenity.id)
        self.assertIn('created_at', amenity_dict)
        self.assertEqual(amenity_dict['created_at'], amenity.created_at.isoformat())
        self.assertIn('updated_at', amenity_dict)
        self.assertEqual(amenity_dict['updated_at'], amenity.updated_at.isoformat())
        self.assertIn('name', amenity_dict)
        self.assertEqual(amenity_dict['name'], amenity.name)

    def test_str(self):
        """Test __str__ method."""
        amenity = Amenity()
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)


if __name__ == '__main__':
    unittest.main()
