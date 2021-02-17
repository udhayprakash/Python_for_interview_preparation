#!/usr/bin/python3
import unittest

from problem import Solution


class TestMinMaxRotation(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()

    def test_empty_array(self):
        self.assertEqual(self.s.max_n_min_rotation([]), (0, 0))

    def test_single_element_array(self):
        self.assertEqual(self.s.max_n_min_rotation([5]), (0, 0))

    def test_two_elements_array(self):
        self.assertEqual(self.s.max_n_min_rotation([5, 6]), (6, 5))

    def test_three_elements_array(self):
        self.assertEqual(self.s.max_n_min_rotation([5, 6, -4]), (17, -2))

    def test_arbitrary_elements_array(self):
        self.assertEqual(self.s.max_n_min_rotation([4, 3, 2, 6]), (26, 16))

    def test_zeros_array(self):
        self.assertEqual(self.s.max_n_min_rotation([0, 0, 0, 0]), (0, 0))

    def test_ones_array(self):
        self.assertEqual(self.s.max_n_min_rotation([1, 1, 1, 1]), (6, 6))

    def test_minus_ones_array(self):
        self.assertEqual(self.s.max_n_min_rotation([-1, -1, -1, -1]), (-6, -6))

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.s


if __name__ == '__main__':
    unittest.main()
