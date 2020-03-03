from django.db import models

import calendar


def month_abbr_to_number(month_abbr):
    # Pass month in abbreviated string format and return month in number format
    month = list(calendar.month_abbr).index(month_abbr)
    if month < 10:
        month = "0" + str(month)  # Add 0 if less than 10
    return month  # return month in number format


def month_number_to_abbr(month_number):
    # Pass month in abbreviated string format and return month in number format
    dog = calendar.month_abbr[month_number]
    # return month in number format
    return dog
