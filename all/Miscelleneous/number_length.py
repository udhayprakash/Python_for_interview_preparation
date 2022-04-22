import math

# number is natural number


def get_number_length(number):
    return len(str(number))


def get_number_length(number):
    return int(math.log10(number)) + 1


def get_number_length(number):
    count = 0
    while number:
        count += 1
        number //= 10
    return count


if __name__ == "__main__":
    assert get_number_length(1) == 1
    assert get_number_length(12) == 2
    assert get_number_length(123) == 3
    assert get_number_length(1232313211123) == 13
