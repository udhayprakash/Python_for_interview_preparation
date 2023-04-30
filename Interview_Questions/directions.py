def absolute_directions(directions):
    opposite = {"North": "South", "South": "North", "East": "West", "West": "East"}
    stack = []

    for direction in directions:
        if stack and stack[-1] == opposite[direction]:
            stack.pop()
        else:
            stack.append(direction)

    return stack


assert absolute_directions(["North", "South"]) == []
assert absolute_directions(["North", "South", "North", "South"]) == []
assert absolute_directions(["North", "South", "North", "South", "North", "South"]) == []
assert absolute_directions(["North", "South", "North"]) == ["North"]
assert absolute_directions(["North", "South", "North", "East"]) == ["North", "East"]
assert absolute_directions(["North", "South", "North", "East"]) == ["North", "East"]
assert absolute_directions(["North", "South", "North", "East", "West"]) == ["North"]
assert absolute_directions(
    ["North", "South", "North", "East", "North", "West", "East"]
) == ["North", "East", "North"]
