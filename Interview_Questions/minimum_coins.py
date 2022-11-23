#!/usr/bin/python3
"""
Problem:

"""


def get_min_coins(given_amount):
    given_amount = given_amount * 100  # converting to pennis
    denominations = {"quarter": 25, "dime": 10, "nickel": 5, "penny": 1}
    coins_choosen = {}
    for coinName, coinValue in denominations.items():
        if given_amount // coinValue == 0:
            coins_choosen[coinName] = 0
        else:
            coins_choosen[coinName] = int(given_amount // coinValue)
            given_amount -= coinValue * (given_amount // coinValue)
    return coins_choosen


if __name__ == "__main__":
    print(get_min_coins(0.24))
    # {'quarter': 0, 'dime': 2, 'nickel': 0, 'penny': 4}
