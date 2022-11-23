def snake_case_to_camel_case(word: str) -> str:
    """
    Coerce snake case to camel case

        Use split with destructuring to grab first word and store rest in list.
    map over the rest of the words passing them to str.capitalize(),
    destructure map list elements into new list with first word at front, and
    finally join them back to a str.

    Note: may want to use `str.title` instead of `str.capitalize`

    :param word: the word or variable to convert
    :return str: a camel cased version of the word
    """

    first, *rest = word.split("_")

    camel_word: list = [first.lower(), *map(str.capitalize, rest)]

    return "".join(camel_word)


print(snake_case_to_camel_case("first_name_is_mr_perfect_2word"))
assert snake_case_to_camel_case("variable") == "variable"
assert snake_case_to_camel_case("variable_name") == "variableName"
assert snake_case_to_camel_case("variable_name_2") == "variableName2"
assert (
    snake_case_to_camel_case("first_name_is_mr_perfect_2word")
    == "firstNameIsMrPerfect2word"
)
