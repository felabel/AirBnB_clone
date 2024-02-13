#!/usr/bin/python3

"""Defines unittests for models/place.py"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test case for Place class."""

    def test_init(self):
        """Test Place initialization."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

        # Test initialization with kwargs
        kwargs = {'id': 'test_id', 'created_at': '2022-02-13T12:00:00.000000',
                  'updated_at': '2022-02-13T12:00:00.000000', 'city_id': 'test_city_id',
                  'user_id': 'test_user_id', 'name': 'test_name', 'description': 'test_description',
                  'number_rooms': 5, 'number_bathrooms': 2, 'max_guest': 10, 'price_by_night': 100,
                  'latitude': 40.7128, 'longitude': -74.006, 'amenity_ids': ['amenity_id1', 'amenity_id2']}
        place_with_kwargs = Place(**kwargs)
        self.assertEqual(place_with_kwargs.id, 'test_id')
        self.assertEqual(place_with_kwargs.created_at, datetime(2022, 2, 13, 12, 0))
        self.assertEqual(place_with_kwargs.updated_at, datetime(2022, 2, 13, 12, 0))
        self.assertEqual(place_with_kwargs.city_id, 'test_city_id')
        self.assertEqual(place_with_kwargs.user_id, 'test_user_id')
        self.assertEqual(place_with_kwargs.name, 'test_name')
        self.assertEqual(place_with_kwargs.description, 'test_description')
        self.assertEqual(place_with_kwargs.number_rooms, 5)
        self.assertEqual(place_with_kwargs.number_bathrooms, 2)
        self.assertEqual(place_with_kwargs.max_guest, 10)
        self.assertEqual(place_with_kwargs.price_by_night, 100)
        self.assertEqual(place_with_kwargs.latitude, 40.7128)
        self.assertEqual(place_with_kwargs.longitude, -74.006)
        self.assertEqual(place_with_kwargs.amenity_ids, ['amenity_id1', 'amenity_id2'])

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        place = Place()
        self.assertIsInstance(place, models.base_model.BaseModel)

    def test_to_dict(self):
        """Test to_dict method."""
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn('__class__', place_dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIn('id', place_dict)
        self.assertEqual(place_dict['id'], place.id)
        self.assertIn('created_at', place_dict)
        self.assertEqual(place_dict['created_at'], place.created_at.isoformat())
        self.assertIn('updated_at', place_dict)
        self.assertEqual(place_dict['updated_at'], place.updated_at.isoformat())
        self.assertIn('city_id', place_dict)
        self.assertEqual(place_dict['city_id'], place.city_id)
        self.assertIn('user_id', place_dict)
        self.assertEqual(place_dict['user_id'], place.user_id)
        self.assertIn('name', place_dict)
        self.assertEqual(place_dict['name'], place.name)
        self.assertIn('description', place_dict)
        self.assertEqual(place_dict['description'], place.description)
        self.assertIn('number_rooms', place_dict)
        self.assertEqual(place_dict['number_rooms'], place.number_rooms)
        self.assertIn('number_bathrooms', place_dict)
        self.assertEqual(place_dict['number_bathrooms'], place.number_bathrooms)
        self.assertIn('max_guest', place_dict)
        self.assertEqual(place_dict['max_guest'], place.max_guest)
        self.assertIn('price_by_night', place_dict)
        self.assertEqual(place_dict['price_by_night'], place.price_by_night)
        self.assertIn('latitude', place_dict)
        self.assertEqual(place_dict['latitude'], place.latitude)
        self.assertIn('longitude', place_dict)
        self.assertEqual(place_dict['longitude'], place.longitude)
        self.assertIn('amenity_ids', place_dict)
        self.assertEqual(place_dict['amenity_ids'], place.amenity_ids)

    def test_str(self):
        """Test __str__ method."""
        place = Place()
        expected_str = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(str(place), expected_str)


if __name__ == '__main__':
    unittest.main()
