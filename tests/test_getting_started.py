import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'scripts')))

import collections
import cv2

import unittest
import numpy as np

from scripts.getting_started import binary_search, bubble_sort

class TestBinarySearch(unittest.TestCase):

    def test_binary_search_in_simple_list(self):
        lst = [1,2,3]
        val = 2
        actual = binary_search.binary_search(lst, val)
        expected = 1
        self.assertEquals(actual, expected)

class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort_simple_list(self):
        lst = [1,2,3]
        actual = bubble_sort.bubble_sort(lst)
        expected = [1,2,3]
        self.assertEquals(actual, expected)

    def test_bubble_sort_unordered_simple_list(self):
        lst = [1,2,3,1,3,2,1]
        actual = bubble_sort.bubble_sort(lst)
        expected = sorted(lst)
        self.assertEquals(actual, expected)
