def StringChallenge(strParam):
    combinations = {"ab": "c", "bc": "a", "ca": "b"}
    i = 0
    while i < len(strParam) - 1:
        print("strParam:", strParam)
        if strParam[i : i + 2] in combinations:
            strParam = (
                strParam[:i] + combinations[strParam[i : i + 2]] + strParam[i + 2 :]
            )
        i += 1

    return strParam


if __name__ == "__main__":
    assert StringChallenge("cab") == "bb"
    assert StringChallenge("bcab") == "ac"
    assert StringChallenge("cccc") == "cccc"
    assert StringChallenge("abcabc") == "cba"
