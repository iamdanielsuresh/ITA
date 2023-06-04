#!/usr/bin/env python3
import unittest
from validation import validate_username
class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_username("validuser",3), True)

    def test_too_short(self):
        self.assertEqual(validate_username("inv", 5), False)

    def test_invalid_char(self):
        self.assertEqual(validate_username("invalid_user",1), False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_username, "user", -1)


#run the test
unittest.main()
