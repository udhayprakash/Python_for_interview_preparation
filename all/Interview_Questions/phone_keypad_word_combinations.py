def is_word(maybe_a_word):
    dictionary = ["good", "home", "end", "hone", "doe"]
    return maybe_a_word in dictionary


def get_words(input_nums, key_map):
    i = 0
    combinations = []
    while i < len(input_nums):
        curr_num = input_nums[i]
        if not combinations:
            combinations = key_map[curr_num]
        else:
            new_comb = []
            for each_chr in key_map[curr_num]:
                for each_comb in combinations:
                    new_comb.append(each_comb + each_chr)
            combinations = new_comb[::]
        i += 1
    combinations = [wrd for wrd in combinations if is_word(wrd)]
    print(combinations)
    return combinations

    # [ [g] [h] [i]    ]
    # [ [gm, gn go] [hm, hn ho] [im in io]    ]

    """
    4 6 6 3

    g
    h
    i

    gm
    gn
    go
    hm
    hn
    """


if __name__ == "__main__":

    """
    +-----+-----+-----+
    |  1  |  2  |  3  |
    |     | abc | def |
    +-----+-----+-----+
    |  4  |  5  |  6  |
    | ghi | jkl | mno |
    +-----+-----+-----+
    |  7  |  8  |  9  |
    | pqrs| tuv | wxyz|
    +-----+-----+-----+
    """

    four_letter_input = [4, 6, 6, 3]  # gnd
    three_letter_input = [3, 6, 3]

    key_map = {
        1: [],
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"],
    }

    get_words(four_letter_input, key_map)
    get_words(three_letter_input, key_map)
