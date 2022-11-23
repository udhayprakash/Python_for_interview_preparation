#!/bin/python3

import json
import math
import os
import random
import re
import sys

#
# Complete the 'getCapitalCity' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING country as parameter.
# API URL: https://jsonmock.hackerrank.com/api/countries?name=<country>
#
import urllib.request

import requests


def getCapitalCity(country):
    url = f"https://jsonmock.hackerrank.com/api/countries?name={country}"
    response = urllib.request.urlopen(url).read()
    responseData = json.loads(response)
    if not responseData["data"]:
        return str(-1)
    return responseData["data"][0]["capital"]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    country = input()

    result = getCapitalCity(country)

    fptr.write(result + "\n")

    fptr.close()
