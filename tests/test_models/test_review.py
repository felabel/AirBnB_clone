#!/usr/bin/python3
"""Defines unnitests for models/review.py."""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review

import unittest
from models.review import Review
from datetime import datetime
import models


class TestReview(unittest.TestCase):
    """Test case for Review class."""

    def test_init(self):
        """Test Review initialization."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

        # Test initialization with kwargs
        kwargs = {'id': 'test_id', 'created_at': '2022-02-13T12:00:00.000000',
                  'updated_at': '2022-02-13T12:00:00.000000', 'place_id': 'test_place_id',
                  'user_id': 'test_user_id', 'text': 'test_text'}
        review_with_kwargs = Review(**kwargs)
        self.assertEqual(review_with_kwargs.id, 'test_id')
        self.assertEqual(review_with_kwargs.created_at, datetime(2022, 2, 13, 12, 0))
        self.assertEqual(review_with_kwargs.updated_at, datetime(2022, 2, 13, 12, 0))
        self.assertEqual(review_with_kwargs.place_id, 'test_place_id')
        self.assertEqual(review_with_kwargs.user_id, 'test_user_id')
        self.assertEqual(review_with_kwargs.text, 'test_text')

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        review = Review()
        self.assertIsInstance(review, models.base_model.BaseModel)

    def test_to_dict(self):
        """Test to_dict method."""
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn('__class__', review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIn('id', review_dict)
        self.assertEqual(review_dict['id'], review.id)
        self.assertIn('created_at', review_dict)
        self.assertEqual(review_dict['created_at'], review.created_at.isoformat())
        self.assertIn('updated_at', review_dict)
        self.assertEqual(review_dict['updated_at'], review.updated_at.isoformat())
        self.assertIn('place_id', review_dict)
        self.assertEqual(review_dict['place_id'], review.place_id)
        self.assertIn('user_id', review_dict)
        self.assertEqual(review_dict['user_id'], review.user_id)
        self.assertIn('text', review_dict)
        self.assertEqual(review_dict['text'], review.text)

    def test_str(self):
        """Test __str__ method."""
        review = Review()
        expected_str = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(str(review), expected_str)


if __name__ == '__main__':
    unittest.main()
