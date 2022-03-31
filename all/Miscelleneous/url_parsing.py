#!/usr/bin/python3
"""
Problem:
Imgur is a popular website for storing digital images. This

Create a function that  takes an imgur link (as a string) and extracts the unique id and type.
Return an object containing the unique id, and a string indicating what type of link it is. 

The link could be pointing to:

    An album (e.g. http://imgur.com/a/cjh4E)
    A gallery (e.g. http://imgur.com/gallery/59np6)
    An image (e.g. http://imgur.com/0zZUNMM)
    An image (direct link) (e.g. http://i.imgur.com/altd8Ld.png)


"""


def imgurParser(url, base_url='imgur.com/'):
    endpoint = url.partion(base_url)[-1]
    if not endpoint:
        return {}
    endpoint = endpoint.split('/')
    if len(endpoint) == 2:
        return {'id': endpoint[1], 'type': 'album' if endpoint[0] == 'a' else 'gallery'}
    return {'id': endpoint[0].split('.')[0], 'type': 'image'}


assert imgurParser(
    "http://imgur.com/a/cjh4E") == {'id': 'cjh4E', 'type': 'album'}
assert imgurParser(
    "http://imgur.com/gallery/59np6") == {'id': '59np6', 'type': 'gallery'}
assert imgurParser(
    "http://imgur.com/0zZUNMM") == {'id': '0zZUNMM', 'type': 'image'}
assert imgurParser(
    "http://i.imgur.com/altd8Ld.png") == {'id': 'altd8Ld', 'type': 'image'}
