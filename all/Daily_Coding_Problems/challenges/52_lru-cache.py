"""
#52
Google

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value.
If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.

get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.

Least Recently Used (LRU) Cache
    - cache is a place that is quick to access where
    you store things that are otherwise slow to access.
    - cache can only ever store a finite amount of things,
    and often is much smaller than whatever it is caching.
    - cache performs really well when it contains the
    thing you are trying to access, and not so well when
    it doesn't.
    - The percentage of times that the cache contains the
    item you are looking for is called the hit rate.
    - The primary factor in hit rate (apart from cache size)
    is replacement strategy.
    - Under the hood, an LRU cache is often implemented by
    pairing a doubly linked list with a hash map.

Strengths:
    1. Super fast accesses.
        - LRU caches store items in order from
          most-recently used to least-recently used.
        - That means both can be accessed in O(1) time.
    2. Super fast updates.
        - Each time an item is accessed, updating the
        cache takes O(1) time.

Weaknesses
    1. Space heavy.
        - An LRU cache tracking nn items requires
        a linked list of length nn, and a hash map
        holding nn items.
        - That's O(n) space, but it's still two
        data structures (as opposed to one).

"""


class LRUCache:
    def __init__(self, capacity):
        self.cache = dict()
        self.orderList = []
        self.capacity = capacity

    def set(self, key, value):
        if key in self.cache:
            # Key is in cache, mark it as recently used item.
            self.orderList.remove(key)
            self.orderList.append(key)
        else:
            if len(self.orderList) >= self.capacity:
                # Cache is full, remove least recentyl used item.
                leastRecent = self.orderList.pop(0)
                del self.cache[leastRecent]
            self.orderList.append(key)

        # Setting the (new) key and value
        self.cache[key] = value

    def get(self, key):
        if key in self.cache:
            # Mark item as recently used
            self.orderList.remove(key)
            self.orderList.append(key)
            return self.cache[key]
        else:
            return -1


def main():
    lruCache = LRUCache(2)
    lruCache.set(1, 1)
    lruCache.set(2, 2)
    print(lruCache.get(1))
    lruCache.set(3, 3)
    print(lruCache.get(2))
    lruCache.set(4, 4)
    print(lruCache.get(1))
    print(lruCache.get(3))
    print(lruCache.get(4))


if __name__ == "__main__":
    main()
