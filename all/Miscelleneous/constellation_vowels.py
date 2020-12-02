#!/usr/bin/python3


def extract_pattern_vowels(pattern):
    pattern_lines = pattern.strip().split('\n')
    line_width = len(pattern_lines[0])
    i = 0
    letters = ''
    while i < line_width:
        if pattern_lines[0][i] == '#':
            letters += '#'
            i += 1
            continue
        combined_pattern = [_line.strip()[i:i + 3] for _line in pattern_lines]
        if combined_pattern == ['*.*', '*.*', '***']:
            letters += 'U'
        elif combined_pattern == ['***', '*.*', '***']:
            letters += 'O'
        elif combined_pattern == ['***', '.*.', '***']:
            letters += 'I'
        elif combined_pattern == ['.*.', '***', '*.*']:
            letters += 'A'
        elif combined_pattern == ['***', '***', '***']:
            letters += 'E'
        else:
            # Ignoring current column as match is not found
            i += 1
            continue
        i += 3
    return letters


if __name__ == '__main__':
    assert extract_pattern_vowels('''
    *.*#***#***#***.*.
    *.*#*.*#.*.#******
    ***#***#***#****.*''') == 'U#O#I#EA'
    
    assert extract_pattern_vowels('''
        *.*#.***#.*.
        *.*#..*.#***
        ***#.***#*.*''')  == 'U#I#A'
