"""
Purpose: Find the angle between hours and minutes handle,
    for a given time.

    NOTE: hours handle drifts for every minute change
"""


def find_angle(h, m):
    """360 -- 12  * 5   == hrs angle
    360 -- 60  * 30   == min angle
    """
    h %= 12
    mins_angle = (360 / 60.0) * m
    hrs_angle = (360 / 12.0) * (h + m / 60.0)
    return abs(hrs_angle - mins_angle)


print(find_angle(5, 30))
assert find_angle(5, 30) == 15.0
assert find_angle(17, 30) == 15
