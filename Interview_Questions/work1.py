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
        m = re.match(r"^[0-9]{2} (\w+)(.*) \(", line)
        if m:
            counts.update(m.groups(1))
            print(m.groups())
pprint(counts)
