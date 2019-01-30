#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_import(self):
        """ Tests for function import """
        self.assertTrue(__import__('6-max_integer').max_integer)

    def test_max_at_back(self):
        """ Tests for the max int at end """
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_at_front(self):
        """ Tests for the max int at beginning """
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_max_in_mid(self):
        """ Tests for the max int in the middle """
        self.assertEqual(max_integer([2, 3, 1]), 3)

    def test_negative(self):
        """ Tests for one negative int """
        self.assertEqual(max_integer([-1, 2, 3]), 3)

    def test_negatives(self):
        """ Tests for mulitple negative ints """
        self.assertEqual(max_integer([-1, -2, 3]), 3)

    def test_only_negatives(self):
        """ Tests with only negative ints """
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_one_element(self):
        """ Tests with only one element list """
        self.assertEqual(max_integer([1]), 1)

    def test_empyt_list(self):
        """ Tests with empty list """
        self.assertEqual(max_integer([]), None)

    if __name__ == '__main__':
        unittest.main()
