#!/usr/bin/python
from security import safe_requests


def get_number_of_movies(sub_str):
    end_point = "https://jsonmock.hackerrank.com/api/movies/search/?Title={}".format(
        sub_str
    )
    response = safe_requests.get(end_point)
    return response.json()["total"]


if __name__ == "__main__":
    assert get_number_of_movies("maze") == 97
    assert get_number_of_movies("harry") == 573
