#!/usr/bin/python3
"Defines unittests for console.py"""

import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

class TestHBNBCommand(unittest.TestCase):
    """Test case for HBNBCommand class."""

    def setUp(self):
        """Set up test environment."""
        self.cli = HBNBCommand()

    def tearDown(self):
        """Tear down test environment."""
        pass

    def test_parse(self):
        """Test parse function."""
        self.assertEqual(parse("create BaseModel"), ["create", "BaseModel"])
        self.assertEqual(parse("show BaseModel 1234"), ["show", "BaseModel", "1234"])
        self.assertEqual(parse("destroy BaseModel 1234"), ["destroy", "BaseModel", "1234"])
        self.assertEqual(parse("all BaseModel"), ["all", "BaseModel"])
        self.assertEqual(parse("count BaseModel"), ["count", "BaseModel"])
        self.assertEqual(parse("update BaseModel 1234 name 'John Doe'"), ["update", "BaseModel", "1234", "name", "'John Doe'"])

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        """Test do_quit method."""
        self.assertTrue(self.cli.do_quit(""))
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        """Test do_EOF method."""
        self.assertTrue(self.cli.do_EOF(""))
        self.assertEqual(mock_stdout.getvalue(), "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        """Test emptyline method."""
        self.cli.emptyline()
        self.assertEqual(mock_stdout.getvalue(), "")

    def test_default(self):
        """Test default method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.default("invalid_command")
            self.assertEqual(mock_stdout.getvalue(), "*** Unknown syntax: invalid_command\n")

    def test_do_create(self):
        """Test do_create method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.do_create("BaseModel")
            self.assertTrue(len(mock_stdout.getvalue()) > 0)

    def test_do_show(self):
        """Test do_show method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.do_show("BaseModel 1234")
            self.assertTrue(len(mock_stdout.getvalue()) > 0)

    def test_do_destroy(self):
        """Test do_destroy method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.do_destroy("BaseModel 1234")
            self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")

    def test_do_all(self):
        """Test do_all method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.do_all("BaseModel")
            self.assertEqual(mock_stdout.getvalue(), "[]\n")

    def test_do_count(self):
        """Test do_count method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.do_count("BaseModel")
            self.assertEqual(mock_stdout.getvalue(), "0\n")

    def test_do_update(self):
        """Test do_update method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.do_update("BaseModel 1234 name 'John Doe'")
            self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")


if __name__ == '__main__':
    unittest.main()
