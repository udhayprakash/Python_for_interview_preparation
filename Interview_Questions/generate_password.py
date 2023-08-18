# write a program to generate strong alphanumeric password from a sentence.
"""
1. sentence should at least 10 characters
2. Should have one small, one capital, one number and one special character
3. Example "I am awesome" -> i@mAw3s0me
"""
import random
import string


def get_random_position(sentence, _used_indices):
    while True:
        index = random.randint(0, len(sentence) - 1)
        if index not in _used_indices:
            return index


def generate_strong_password(input_str):
    input_str = input_str.strip().lower().replace(" ", "")
    if len(input_str) < 10:
        return "INNVALID INPUT  STR. NEEEd "
    used_indices = []

    # for each in (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.whitespace ):
    rand_index = get_random_position(input_str, used_indices)
    used_indices.append(rand_index)
    if input_str[rand_index] not in string.ascii_lowercase:
        input_str = (
            input_str[:rand_index]
            + input_str[rand_index].lower()
            + input_str[rand_index + 1 :]
        )
    print("after lowr", input_str)

    rand_index = get_random_position(input_str, used_indices)
    used_indices.append(rand_index)
    if input_str[rand_index] not in string.ascii_uppercase:
        input_str = (
            input_str[:rand_index]
            + input_str[rand_index].upper()
            + input_str[rand_index + 1 :]
        )
    print("after upper", input_str)

    rand_index = get_random_position(input_str, used_indices)
    used_indices.append(rand_index)
    charnum_map = {"a": "@", "e": "3", "i": "1", "l": "1", "o": "0"}
    for each_index, each_char in enumerate(input_str):
        if charnum_map.get(each_char) and each_index not in used_indices:
            input_str = (
                input_str[:each_index]
                + charnum_map[each_char]
                + input_str[each_index + 1 :]
            )
            # used_indices.append(each_index)
            # break
    # else:
    #     input_str = input_str[:rand_index] + random.choice(charnum_map.keys()) + input_str[rand_index+ 1:]
    # if  input_str[rand_index] not in string.digits:
    #     input_str = input_str[:rand_index] + random.choice(string.digits) + input_str[rand_index+1:]
    print("after digits", input_str)

    # rand_index = get_random_position(input_str, used_indices)
    # used_indices.append(rand_index)
    # if  input_str[rand_index] not in string.whitespace:
    #     input_str = input_str[:rand_index] + random.choice(string.whitespace) + input_str[rand_index+1:]
    # print("after white", input_str)

    return input_str


if __name__ == "__main__":
    user_sentence = input("Enter the sentence:")
    print(generate_strong_password(user_sentence))
