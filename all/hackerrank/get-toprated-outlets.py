#!/bin/python3

import math
import os
import random
import re
import sys
import requests
from collections import defaultdict
#
# Complete the 'getTopRatedFoodOutlets' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/food_outlets?city=<city>&page=<pageNumber>
#
# The function is expected to return an array of strings.
# The function accepts only city argument (String).
#

def getTopRatedFoodOutlets(city):
    results = defaultdict(list)
    pagenumber = 1
    highestRating = 0
    while True:
        URL = f'https://jsonmock.hackerrank.com/api/food_outlets?city={city}&page={pagenumber}'
        response = requests.get(URL)
        response.raise_for_status()
        r_data = response.json()
        for each_record in r_data['data']:
            each_rating = each_record["user_rating"]["average_rating"]
            if each_rating >= highestRating:
                results[each_rating].append(each_record["name"])
            if each_rating > highestRating:
                highestRating = each_rating
        if r_data['page'] == r_data['total_pages']:
            break
        pagenumber+= 1
        
    return results[highestRating]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    city = input()

    result = getTopRatedFoodOutlets(city)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
