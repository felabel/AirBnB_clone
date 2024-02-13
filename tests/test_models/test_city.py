#!/usr/bin/pyton3
"""Defies unittests for models/city.py"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City

class TestCity(unittest.TestCase):
    """Test case for City class."""

    def test_init(self):
        """Test City initialization."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

        # Test initialization with kwargs
        kwargs = {'id': 'test_id', 'created_at': '2022-02-13T12:00:00.000000',
                  'updated_at': '2022-02-13T12:00:00.000000', 'state_id': 'test_state_id',
                  'name': 'test_name'}
        city_with_kwargs = City(**kwargs)
        self.assertEqual(city_with_kwargs.id, 'test_id')
        self.assertEqual(city_with_kwargs.created_at, datetime(2022, 2, 13, 12, 0))
        self.assertEqual(city_with_kwargs.updated_at, datetime(2022, 2, 13, 12, 0))
        self.assertEqual(city_with_kwargs.state_id, 'test_state_id')
        self.assertEqual(city_with_kwargs.name, 'test_name')

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        city = City()
        self.assertIsInstance(city, models.base_model.BaseModel)

    def test_to_dict(self):
        """Test to_dict method."""
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn('__class__', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIn('id', city_dict)
        self.assertEqual(city_dict['id'], city.id)
        self.assertIn('created_at', city_dict)
        self.assertEqual(city_dict['created_at'], city.created_at.isoformat())
        self.assertIn('updated_at', city_dict)
        self.assertEqual(city_dict['updated_at'], city.updated_at.isoformat())
        self.assertIn('state_id', city_dict)
        self.assertEqual(city_dict['state_id'], city.state_id)
        self.assertIn('name', city_dict)
        self.assertEqual(city_dict['name'], city.name)

    def test_str(self):
        """Test __str__ method."""
        city = City()
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)


if __name__ == '__main__':
    unittest.main()


