#!/usr/bin/python3

"""unittest for console"""

import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """
    Tests the console functions
    """
    @classmethod
    def setUpClass(cls):
        """
        set up the tests
        """
        cls.conso = HBNBCommand()

    @classmethod
    def teardown(cls):
        """
        clean up or tear down a system or environment.
        """
        del cls.conso

    @classmethod
    def tearDown(self):
        """
        called after each test method has been run.
        Remove temporary file
        """
        try:
            os.remove(file.json)
        except Exception:
            pass

    def test_pep8_conform(self):
        """
        module console.p conforms to pep8 standards
        """
        pep_style = pep8.StyleGuide(quite=True)
        conso_style = pep_style.check_files(["console.py"])
        self.assertEqual(conso_style.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring_console_module(self):
        """
        verify docstring exists
        """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline__doc__)
        self.assertIsNotNone(HBNBCommand.do_create__doc__)
        self.assertIsNotNone(HBNBCommand.help_create__doc__)
        self.assertIsNotNone(HBNBCommand.do_show__doc__)
        self.assertIsNotNone(HBNBCommand.help_show__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy__doc__)
        self.assertIsNotNone(HBNBCommand.help_destroy__doc__)
        self.assertIsNotNone(HBNBCommand.do_all__doc__)
        self.assertIsNotNone(HBNBCommand.help_all__doc__)
        self.assertIsNotNone(HBNBCommand.do_count__doc__)
        self.assertIsNotNone(HBNBCommand.help_count__doc__)
        self.assertIsNotNone(HBNBCommand.do_update__doc__)
        self.assertIsNotNone(HBNBCommand.help_update__doc__)

    def test_create(self):
        """
        program produces the expected output message when the
        user enters the "create" command without specifying a
        class name.
        """
        with patch('sys.stdout', new_str=StringIO()) as f:
            self.conso.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())


if __name__ == "__main__":
    unittest.main()
