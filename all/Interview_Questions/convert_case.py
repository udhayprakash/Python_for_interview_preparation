import enum
import re
from threading import get_ident


def snake_case_to_camel_case(given_str):
    if not ("_" in given_str):
        return given_str
    start_index = 0
    new_str = given_str[:start_index]
    for m in re.finditer("_", given_str):
        substr = given_str[start_index : m.start()].title()
        start_index = m.start() + 1
        new_str += substr
    else:
        print("=^^", new_str)
        new_str += given_str[start_index:].title()
    print(given_str, "====>", new_str)
    return new_str


# print(snake_case_to_camel_case("variable_name_2234"))
assert snake_case_to_camel_case("variable") == "variable"
assert snake_case_to_camel_case("variable_name") == "variableName"
# assert snake_case_to_camel_case("variable_name_2") == "variableName2"
