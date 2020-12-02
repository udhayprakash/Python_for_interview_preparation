#!/usr/bin/python3
"""
Purpose:
    A company pays the salary to its customers on hourly work basis as per the following criteria.

    First 8 hours Rs. 20 per hour

    Next 4 hours Rs. 30 per hour
    Next 6 hours Rs. 50 per hour

    For more than 18 hours Rs. 100 per hour

    Write the code to input number of hours worked in a day by a worker. Calculate and print his monthly

    salary considering that he works for same no. of hours daily
"""
hours_worked_per_day = float(input('Enter the number of hours worked:'))

salary_per_day = 0
if hours_worked_per_day > 18:
    salary_per_day += (hours_worked_per_day - 18) * 100
    hours_worked_per_day = 18
if 12 < hours_worked_per_day <= 18:
    salary_per_day += (hours_worked_per_day - 12) * 50
    hours_worked_per_day = 12
if 8 < hours_worked_per_day <= 12:
    salary_per_day += (hours_worked_per_day - 8) * 30
    hours_worked_per_day = 8
if hours_worked_per_day <= 8:
    salary_per_day += hours_worked_per_day * 20

print('salary_per_day:', salary_per_day)