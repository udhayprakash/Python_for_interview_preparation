import re


def howMany(sentence):
    final_words = []
    for word in sentence.split():
        word = word.strip(".,?!")
        if word and not re.sub("[a-zA-Z-]", "", word):
            final_words.append(word)
    # print(final_words)
    return len(final_words)


assert howMany("He is a good programmer, he won first-place.") == 8
assert howMany("All test-cases should pass.") == 4
assert howMany("jds lkdf kd[sa fkldsf, test-cases shou}ld pass.") == 5
