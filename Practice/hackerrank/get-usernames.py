#!/bin/python3

import json
import math
import os
import random
import re
import sys

#
# Complete the 'getUsernames' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER threshold as parameter.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/article_users?page=<pageNumber>
import urllib.request


def getUsernames(threshold):
    result = []
    pageNumber = 1
    while True:
        URL = f"https://jsonmock.hackerrank.com/api/article_users?page={pageNumber}"
        response = urllib.request.urlopen(URL)
        response_data = json.loads(response.read())
        for eachrecord in response_data["data"]:
            if eachrecord["submission_count"] > threshold:
                result.append(eachrecord["username"])
        pageNumber += 1
        if response_data["page"] == response_data["total_pages"]:
            break
        print(eachrecord)
    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    threshold = int(input().strip())

    result = getUsernames(threshold)

    fptr.write("\n".join(result))
    fptr.write("\n")

    fptr.close()
