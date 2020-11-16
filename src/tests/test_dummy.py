#Test for unittest/ci/c
import os
import re
from src.main import add
import unittest

class dummytest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)