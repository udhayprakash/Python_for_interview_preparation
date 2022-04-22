#!/usr/bin/python
"""
Purpose: Unit test script for a_Linked_list.py file
"""

import unittest

from a_Linked_list import SingleLinkedList


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sl_list = SingleLinkedList()

    # def testing_insert_tail(self):
    #     self.assertEqual(self.sl_list.insert_tail(3), 4)

    def tearDown(self) -> None:
        del self.sl_list


if __name__ == "__main__":
    unittest.main()
