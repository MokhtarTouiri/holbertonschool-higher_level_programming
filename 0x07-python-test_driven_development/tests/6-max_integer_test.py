#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
max_integer = __import__('6-max_integer').max_integer
import unittest
""" CLASS """
class TestMaxInteger(unittest.TestCase):
    """ DEF """
    def max_integer(self):
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual('len(list) == 0'.max_integer(), 'None')
""" IF """
if __name__ == '__main__':
    unittest.main()

