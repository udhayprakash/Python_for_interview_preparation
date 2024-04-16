#!/usr/bin/python3
"""
profiling steps
    1. pip install snakeviz
    2. python -m cProfile -o temp.dat movie_titles.py
    3. snakeviz temp.dat

"""


import json
import urllib.request
from security import safe_requests


def time_taken(func):
    def inner(*args, **kwargs):
        import time

        start = time.process_time()
        result = func(*args, **kwargs)
        print(f"TIME TAKEN:{time.process_time() - start}")
        return result

    return inner


@time_taken
def getMovieTitles(substr):

    page = 1
    titles = []
    while True:
        url = f"https://jsonmock.hackerrank.com/api/movies/search/?Title={substr}&page={page}"
        response_data = safe_requests.get(url).json()
        if response_data["page"] == response_data["total_pages"]:
            break
        titles.extend([each["Title"] for each in response_data["data"]])
        page += 1

    return sorted(titles)


@time_taken
def getMovieTitles2(substr):
    import json
    import urllib.request

    page = 1
    titles = []
    while True:
        url = f"https://jsonmock.hackerrank.com/api/movies/search/?Title={substr}&page={page}"
        response = urllib.request.urlopen(url).read()
        response_data = json.loads(response)
        if response_data["page"] == response_data["total_pages"]:
            break
        titles.extend([each["Title"] for each in response_data["data"]])
        page += 1

    return sorted(titles)


@time_taken
def getMovieTitles3(substr):
    import re
    import urllib.request

    page = 1
    titles = []
    while True:
        url = f"https://jsonmock.hackerrank.com/api/movies/search/?Title={substr}&page={page}"
        response = str(urllib.request.urlopen(url).read())
        titles += re.findall('"Title":"(.+?)",', response)
        current_page = re.search(r'"page":(\d+),', response).group(1)
        total_pages = ""
        if not total_pages:
            total_pages = re.search(r'"total_pages":(\d+),', response).group(1)
        if current_page == total_pages:
            break
        page += 1

    return sorted(titles)


def build_query(base_url, params):
    for p in params:
        base_url += "&{}"


def json_from_url(url):
    request = urllib.request.urlopen(url)
    response = request.read()
    encoding = request.info().get_content_charset("utf-8")
    json_data = json.loads(response.decode(encoding))
    return json_data


@time_taken
def get_all_titles():
    url_base = (
        "https://jsonmock.hackerrank.com/api/movies/search/?Title=spiderman&page="
    )
    page_num = 1

    max_pages_reached = False
    titles = []

    while not max_pages_reached:
        url = url_base + str(page_num)
        data = json_from_url(url)

        max_pages = data["total_pages"]

        if page_num == max_pages:
            max_pages_reached = True
        else:
            for movie_object in data["data"]:
                titles.append(movie_object["Title"])
            page_num += 1

    return titles


if __name__ == "__main__":
    getMovieTitles("spiderman")
    getMovieTitles2("spiderman")
    getMovieTitles3("spiderman")
    get_all_titles()
