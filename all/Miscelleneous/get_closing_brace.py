#!/usr/bin/python3
"""
Purpose: 
"""
def get_closing_paren(sentence, opening_paren_index):
    open_nested_parens = 0

    for position in range(opening_paren_index + 1, len(sentence)):
        char = sentence[position]

        if char == '(':
            open_nested_parens += 1
        elif char == ')':
            if open_nested_parens == 0:
                return position
            else:
                open_nested_parens -= 1

    raise Exception("No closing parenthesis :(")


if __name__ == '__main__':
    sentence = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
    print(get_closing_paren(sentence, 10)) # 79