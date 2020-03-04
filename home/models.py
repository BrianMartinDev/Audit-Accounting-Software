from django.db import models
try:
    from array import array
    import pytesseract
    import json
    import calendar
except ImportError:
    from array import array
    import pytesseract
    import json
    import calendar


def month_abbr_to_number(month_abbr):
    # Pass month in abbreviated string format and return month in number format
    abbreviation_to_num = list(calendar.month_abbr).index(month_abbr)
    if abbreviation_to_num < 10:
        abbreviation_to_num = "0" + str(abbreviation_to_num)  # Add 0 if less than 10
    return abbreviation_to_num  # return month in number format


def month_number_to_abbr(month_number):
    # Pass month num and return abbreviated string format
    month_num_abbreviated = calendar.month_abbr[month_number]
    # returns abbreviated string format
    return month_num_abbreviated


# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\BMART\AppData\Local\Tesseract-OCR\tesseract.exe'

testimage = pytesseract.image_to_string('testimage.PNG')

# insert into a list by removing white space

z = testimage.split()
print(z)
