import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([1, 6, 8, 15], 0, "test"), 1)
        self.assertEqual(arrs.get([1, 6, 8, 15], -7, "test"), "test")


    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 16, 29], -5, -1), [2, 3, 4, 16])
        self.assertEqual(arrs.my_slice([1, 2, 3], -7, 2), [1, 2])
        self.assertEqual(arrs.my_slice([], -7, -1), [])
