#!/usr/bin/python3
"""
Purpose:
    Your program should take a single path as input.
    It will read in the names of the files and sort the files into a series
    of frame sequences.
    A frame sequence is a tuple that contains a file name with a frame
    qualifier (%d is fine for now), a first and last frame number, and
    a frame count.
    For example, given the following files:
        mvr_1000.v01.1100.exr
        mvr_1000.v01.1101.exr
        mvr_1000.v01.1103.exr
        mvr_1000.v01.1104.exr
        abb5670_v01.0000.00000003.dpx
        abb5670_v01.0000.00000004.dpx
        abb5670_v01.0000.00000005.dpx

    The output from the program should be this:  [[mvr_1000.v01.%d.exr, 1100, 1104, 4], [abb5670_v01.0000.%d.dpx, 3, 5, 3]]

    The frame number will always be the last portion of the file name immediately before the file extension.

    The code should be able to handle gaps of any size within the frame ranges.  Treat them as a single frame range.

    Multiple sequences should be expected within the directory.  You do not need to handle subdirectories,
    just the files in the path provided.

    Any files that don't appear to be part of a frame sequence should be ignored.
"""
import re

# imports
from collections import defaultdict


# Functions
def myfunc(given_files):
    result = defaultdict(list)
    for file in given_files:
        pattern = re.search(r"(.*)\.(\d+)\.(\w+)$", file)
        if pattern:
            prefix, num, extn = pattern.groups()
            result[".".join([prefix, "%d", extn])].append(int(num))

    final = []
    for expr, nums in result.items():
        if len(nums) == 1:
            # skipping files which dont have this pattern
            continue
        nums.sort()
        final.append([expr, nums[0], nums[-1], len(nums)])
    print(final)
    return final


if __name__ == "__main__":
    files = [
        "mvr_1000.v01.1100.exr",
        "mvr_1000.v01.1103.exr",
        "mvr_1000.v01.1101.exr",
        "mvr_1000.v01.1104.exr",
        "abb5670_v01.0000.00000004.dpx",
        "abb5670_v01.0000.00000003.dpx",
        "abb5670_v01.0000.00000005.dpx",
    ]

    expected_output = [
        ["mvr_1000.v01.%d.exr", 1100, 1104, 4],
        ["abb5670_v01.0000.%d.dpx", 3, 5, 3],
    ]

    assert myfunc(files) == expected_output
