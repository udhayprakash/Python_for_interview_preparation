def minimum_suffix(words):
    min_wrd = min(words, key=len)
    i = 1
    while True:
        suffic = min_wrd[-i:]
        if all([word.endswith(suffic) for word in words]):
            i += 1
        else:
            if i == 1:
                return ""
            return min_wrd[-i + 1 :]
    return ""


print(
    minimum_suffix(["renting", "painting", "denting", "flaunting", "venting"])
    == "nting"
)
print(minimum_suffix(["running", "renting", "painting", "bling", "ping"]) == "ing")
print(minimum_suffix(["run", "renting", "painting", "bling", "ping"]) == "")
