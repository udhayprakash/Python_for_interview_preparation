def permutations(given_str, substr="", result=None):
    if not result:
        result = []
    if not given_str:
        return substr

    index = 0
    while index < len(given_str):
        new_substr = given_str[0:index] + given_str[index + 1 :]
        result_substr = permutations(new_substr, substr + given_str[index], result)
        if result_substr:
            result.append(result_substr)
        print("\nresult substr", result_substr)
        index += 1

    print("final", result)
    return result


print(permutations("abc"))
