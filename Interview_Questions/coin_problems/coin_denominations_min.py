"""
Purpose:
    The challenge - we want you to design a cash register algorithm that,
    given an item price and the amount a customer paid for it, returns the optimal amount of change for that customer.
    i.e. write a function, make_change, that takes two arguments:
        item price
        amount paid
    And returns an optimized amount of change.

    e.g. if the item price is $13.92, and the amount paid is $20, we would want to get back
        1 $5.00 bill
        1 $1.00 bill
        1 nickel
        3 pennies

    Rather than something like 608 pennies.
    Assume that the cash register has an unlimited amount of coins and bills - we can assume that we have denominations going from pennies up to 20 dollar bills.
"""
DENOMINATIONS = {
    500: "5D",
    200: "2D",
    100: "1D",
    50: "50c",
    25: "25c",
    10: "10c",
    5: "5c",
    2: "2c",
    1: "1c",
}


def user_friendly_display(change_cts):
    result = ""
    for den, ct in change_cts.items():
        result += f"{ct} {DENOMINATIONS.get(den, den)};"
    return result.rstrip(";")


def make_change(item_price, amount_paid):
    if item_price > amount_paid:
        raise Exception("Insufficient Amount")
    change = (amount_paid - item_price) * 100
    change_count = {}

    for denomination in DENOMINATIONS:
        if change >= denomination:
            count = int(change // denomination)
            change_count[denomination] = count
            change = change % denomination

    return user_friendly_display(change_count)


assert make_change(18, 20) == "1 2D"
assert make_change(13.91, 20) == "1 5D;1 1D;1 5c;2 2c"
assert make_change(18, 20) == "1 2D"
assert make_change(18.9, 20) == "1 1D;1 10c"
assert make_change(20, 20) == ""
assert make_change(20, 21) == "1 1D"
try:
    make_change(21, 20)
except Exception as ex:
    assert str(ex) == "Insufficient Amount"

assert make_change(13.91, 20) == "1 5D;1 1D;1 5c;2 2c"
