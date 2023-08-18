"""
Problem: BO - FIX Parsing

A log file represents a trade per line, and each trade is composed of 5 fields

	35  - msgtype
	34 	- seqNum( Sequence Number: Always +ve integres. for a given day, starts with 1, uniq for each trade)
	11 	- OrderID
	99 	- Qty (+ve is Buys/ -ve is sells)
	50 	- price

Tasks
	Given a list of log dump lines for a particular day,
		1. Print the earliest missing sequence number
		2. Print qty weighted average buy price
		3. Print qty weighted average sell price

company - SQuarePoint Capital
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'completeTask' function below.
#
# The function accepts STRING_ARRAY logLines as parameter.
#
from pprint import pp
from typing import List


def complete_task(log_lines: List[str]):
    result = {}
    for line in log_lines:
        for each in line.split("|"):
            field, value = each.split("=")
            if field != "11":
                field, value = map(float, (field, value))
            result.setdefault(field, []).append(value)

    pp(result)
    i = 1
    seqNums = sorted(result.get(34.0, []))
    while i < len(seqNums):
        if seqNums[i] - seqNums[i - 1] != 1:
            print("Missing Seqnum", seqNums[i - 1] + 1)
            break
        i += 1
    else:
        print("No missing Sequence number")

    # qty weighted price = summation (price * qty) / summation(qty)
    qtys = result.get(99.0, [])
    prices = result.get(50.0, [])

    # buys
    buys_sum = sum([(prices[i] * qty) for i, qty in enumerate(qtys) if qty > 0])
    weighted_buys_avg = buys_sum / sum([qty for qty in qtys if qty > 0])

    # Sells
    sells_sum = sum([(prices[i] * qty) for i, qty in enumerate(qtys) if qty < 0])
    weighted_sells_avg = sells_sum / sum([qty for qty in qtys if qty < 0])

    print("qty weighted avg buy price", weighted_buys_avg)
    print("qty weighted avg sells price", weighted_sells_avg)


def complete_task(log_lines: str) -> None:
    seqNums = re.findall(r"\|?34=(\d+)\|+?", log_lines)
    seqNums = sorted(map(int, seqNums))

    i = 1
    while i < len(seqNums):
        if seqNums[i] - seqNums[i - 1] != 1:
            print("Missing Seqnum", seqNums[i - 1] + 1)
            break
        i += 1
    else:
        print("No missing Sequence number")

    # qty weighted price = summation (price * qty) / summation(qty)
    qtys = sorted(map(int, re.findall(r"\|?99=(-?\d+)", log_lines)))
    prices = sorted(map(float, re.findall(r"\|?50=(\d+\.\d+)\|+?", log_lines)))

    # buys
    buys_sum = sum([(prices[i] * qty) for i, qty in enumerate(qtys) if qty > 0])
    weighted_buys_avg = buys_sum / sum([qty for qty in qtys if qty > 0])

    # Sells
    sells_sum = sum([(prices[i] * qty) for i, qty in enumerate(qtys) if qty < 0])
    weighted_sells_avg = sells_sum / sum([qty for qty in qtys if qty < 0])

    print("qty weighted avg buy price", weighted_buys_avg)
    print("qty weighted avg sells price", weighted_sells_avg)


if __name__ == "__main__":
    complete_task(
        """
        35=0|11=xavAxsdq1252|34=1|50=10.23|99=65
        35=0|11=weAxsdq1212|34=2|50=10.10|99=100
        35=0|11=poqAxsdq1222|34=5|50=9.05|99=-35
        35=0|11=g32Axsdq1262|34=10|50=8.70|99=-1000
        34=3|35=0|11=mxAxsdq1251|50=13.80|99=75
    """
    )
