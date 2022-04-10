#!/usr/bin/python3
"""
Problem Statement: 
	Given a string S consisting of N lowercase letters, 
	retun minimum number of letters that must be deleted to obtain a word in 
	which every letter ocuurs a unique number of times. 
	we only care about occurrenes of letters that appear at least one in result
	
"""

def solution(S):
    if (not S) or (len(set(S)) == 1): return 0
    counts = {}
    for ch in S:
        counts.setdefault(ch, 0)
        counts[ch] += 1
    uniqueCounts = []
    deletecounts = 0
    for ch, count in counts.items():
        if count in uniqueCounts:
            if (count -1) in uniqueCounts:
                deletecounts += count
            else:
                deletecounts += 1
                uniqueCounts.append(count-1)
        else:
            uniqueCounts.append(count)
    return deletecounts
	
	
assert solution('aaaabbbb') == 1 # {'a':4, 'b':4} remove one b
assert solution('ccaaffddecee') == 6 
assert solution('eeee') == 0
assert solution('example') == 4