def closestMultiple(base, target):
    return (target // base) * base


print(closestMultiple(2048, 1000) == 0)
print(closestMultiple(2048, 2000) == 0)
print(closestMultiple(2048, 4000) == 2048)
print(closestMultiple(2048, 5000) == 4096)
print(closestMultiple(2048, 7000) == 6144)
