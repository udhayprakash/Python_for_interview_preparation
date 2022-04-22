def getMin(s):
    neededCount = 0
    braces_found = []
    for each_char in s:
        if each_char == "(":
            braces_found.append(each_char)
        elif each_char == ")":
            if (not braces_found) or (braces_found[-1] != "("):
                neededCount += 1
            else:
                braces_found.pop()
    if braces_found:
        neededCount += 1
    return neededCount


if __name__ == "__main__":
    assert getMin("(") == 1
    assert getMin("()") == 0
    assert getMin("())") == 1
    assert getMin("(())") == 0
    assert getMin("(())(") == 1
    assert getMin(")(())(") == 2
