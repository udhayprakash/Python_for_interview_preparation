import unittest

import pandas as pd
from solution import find_groups_with_value


class Test(unittest.TestCase):
    def test01_basic(self):
        """Test a basic example"""
        df = pd.DataFrame({"a": [1, 1, 2, 2, 3], "b": [7, 5, 8, 6, 7]})
        expected = pd.DataFrame({"a": [1, 1, 3], "b": [7, 5, 7]}, index=[0, 1, 4])
        actual = find_groups_with_value(df, 7)
        pd.testing.assert_frame_equal(actual, expected)

    # def test02_basic_no_match(self):
    #     """ Test a basic example with no matches
    #     """
    #     df = pd.DataFrame({
    #         "a": [1, 1, 2, 2, 3],
    #         "b": [7, 5, 8, 6, 7]
    #     })
    #     expected = pd.DataFrame(
    #         columns=["a", "b"],
    #         dtype="int64",
    #         index=pd.Index([], dtype="int64")
    #     )
    #     actual = find_groups_with_value(df, 42)
    #     print("-actual\n", actual)
    #     print("-expected\n", expected)
    #     pd.testing.assert_frame_equal(actual, expected)

    # def test03_non_contiguous(self):
    #     """ Test a non-contiguous example
    #     """
    #     df = pd.DataFrame({
    #         "a": [1, 1, 2, 1, 3],
    #         "b": [7, 5, 8, 6, 7]
    #     })
    #     expected = pd.DataFrame({
    #         "a": [1, 1, 1],
    #         "b": [7, 5, 6]
    #     }, index=[0, 1, 3])
    #     actual = find_groups_with_value(df, 6)
    #     pd.testing.assert_frame_equal(actual, expected)
