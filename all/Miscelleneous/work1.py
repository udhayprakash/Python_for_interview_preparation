# import re
# payload_str = '''{
# 	"a": {
# 		"a1": {
# 			"b0": "someyo",
# 			"b1": {
# 				"c1": "car"
# 			},
# 			"test":"name",
# 		}
# 	},
# 	"b": {
# 	}

# }'''
# # create pattern
# pattern = r''
# for each_node in 'a/a1/b1/c1'.split('/'):
#     pattern += each_node + '.+'
# pattern = pattern.rstrip('+') + ':(.*?)\n.+'

# print("pattern=", pattern)  # 'a.+a1.+b1.+c1.:(.*?)\n.+'
# print("result=", re.search(pattern, payload_str, re.DOTALL).group(1))  # "car"

"""
import random

def shuffler(mylist):
	new_list = []
	while len(mylist):
		rand_pos = random.randint(0, len(mylist))
		new_list.append(mylist[rand_pos])
		del mylist[rand_pos]
	return new_list


print(shuffler(['a', 'b', 'c', 'd', 'e']))
"""

import re
from collections import Counter
from pprint import pprint

path = r"C:\Users\Amma\Documents\jobs.txt"
with open(path) as fh:
    data = fh.readlines()

counts = Counter()
for line in data:
    line = line.strip()
    if line:
        m = re.match("^[0-9]{2} (\w+)(.*) \(", line)
        if m:
            counts.update(m.groups(1))
            print(m.groups())
pprint(counts)
