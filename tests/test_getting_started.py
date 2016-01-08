import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'scripts')))

import collections
import cv2

import unittest
import numpy as np

import scripts.getting_started

class TestBinarySearch(unittest.TestCase):

    """ binary search tests """
    def test_binary_search_in_simple_list(self):
        lst = [1,2,3]
        val = 2
        actual = scripts.getting_started.binary_search(lst, val)
        expected = 1
        self.assertEquals(actual, expected)

class 
