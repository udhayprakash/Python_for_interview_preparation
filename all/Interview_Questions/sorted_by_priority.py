"""
Question: Combined Dictionaries

You are provided a list of dictionaries, sorted by priority from
highest to lowest. Each dictionary has strings as keys and the
values are either integers or nested dictionaries. Assume that
value type for existing keys is the same for all dictionaries.

The goal for this question is to aggregate the list of
dictionaries into a single Dictionary.
"""
import copy

# Sorted by priority from highest to lowest
data = [
    {"a": 1, "b": 2, "c": {"d": 4}},  # obj one
    {"c": {"d": 2, "e": 3, "f": 4}, "i": 15},  # obj two
    {"b": 3, "c": {"e": 2, "g": 5}, "h": 10, "k": {"l": {"m": {"n": 12}}}},  # obj three
    {"j": 20, "k": {"l": {"m": {"n": 15, "o": 13}, "p": 18}}},  # obj four
]

# Expected output
expected = {
    "a": 1,  # from obj one
    "b": 2,  # from obj one
    "c": {  # output["c"] will always be a mapping
        "d": 4,  # from obj one
        "e": 3,  # from obj two
        "f": 4,  # from obj two
        "g": 5,  # from obj three
    },
    "h": 10,  # from obj three
    "i": 15,  # from obj two
    "j": 20,  # from obj four
    "k": {  # output["k"] will always be a mapping
        "l": {  # output["k"]["l"] will always be a mapping
            "m": {  # output["k"]["l"]["m"] will always be a mapping
                "n": 12,  # from obj three
                "o": 13,  # from obj four
            },
            "p": 18,  # from obj four
        }
    },
}


class Solution:
    """Enter your solution here"""

    def combineAll(self, data):
        if not data:
            return {}
        if len(data) == 1:
            return data[0]
        result = data[0]
        for currDict in data[1:]:
            result = self.combineTwo(hi=result, lo=currDict)
        return result

    def combineTwo(self, hi, lo):
        hi = copy.deepcopy(hi)
        for k, v in lo.items():
            if k in hi:
                if isinstance(v, dict):
                    hi[k] = self.combineTwo(hi[k], v)
                continue
            hi[k] = v
        return hi


# TEST SUITE
def main():
    print("run tests...")

    sol = Solution()

    # test 2-way merge with empty data
    assert sol.combineTwo({}, {}) == {}

    # test 2-way merge with partially empty data
    one = {"a": 1, "c": 3}
    assert sol.combineTwo(one, {}) == one
    assert sol.combineTwo({}, one) == one

    # test 2-way merge with no overlap
    hi = {"a": 1, "c": 3}
    lo = {"b": 2, "d": 4}
    result = sol.combineTwo(hi, lo)
    assert result == {"a": 1, "b": 2, "c": 3, "d": 4}

    # test 2-way merge with overlap
    hi = {"a": 1, "b": 2}
    lo = {"a": 3, "c": 3}
    result = sol.combineTwo(hi, lo)
    assert result == {"a": 1, "b": 2, "c": 3}

    # test 2-way merge with overlap + nesting
    hi = {"a": {"b": {"c": 1}}}
    lo = {"a": {"b": {"c": 2}}, "d": 2}
    result = sol.combineTwo(hi, lo)
    assert result == {"a": {"b": {"c": 1}}, "d": 2}

    # one more test 2-way merge with overlap + nesting
    hi = {"a": {"b": {"c": 1}}}
    lo = {"a": {"b": {"c": 2, "j": 10}}, "d": 2}
    result = sol.combineTwo(hi, lo)
    assert result == {"a": {"b": {"c": 1, "j": 10}}, "d": 2}

    # test n-way merge with empty data
    result = sol.combineAll([])
    assert result == {}

    # test n-way merge with overlap
    result = sol.combineAll([{"a": 1, "b": 1}, {"b": 2, "c": 2}, {"c": 3, "d": 3}])
    assert result == {"a": 1, "b": 1, "c": 2, "d": 3}

    # test n-way merge with repeated overlap
    result = sol.combineAll([{"a": i, "b": i, "c": i, "d": i} for i in range(1000)])
    assert result == {"a": 0, "b": 0, "c": 0, "d": 0}

    # test n-way merge with overlap + nesting
    result = sol.combineAll(data)
    assert result == expected

    print("tests finished.")


if __name__ == "__main__":
    main()
