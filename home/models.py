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


def picture_to_date(picture):
    # Month test
    month_index_counter = 0
    month_passed = ""
    month_failed = 0
    keep_going = True
    months_array = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

    while keep_going:
        for month_passed in months_array:
            if month_passed in picture:
                # search through picture and find month
                break

        month_failed = month_failed + 1
        print("try # ", month_failed)
        # Get Month from list
        for month_in_array in months_array:  # Use all 12 months to find the month in the list
            if month_in_array in picture:  # If month is Feb and is in list
                month_index_counter = picture.index(month_in_array) + 1  # used to find index of feb
                print(month_index_counter)
                print(month_in_array)
                break
        if month_in_array == month_passed:

            month_to_num = month_abbr_to_number(month_in_array)
            print("Passed Month " + str(month_to_num))

            keep_going = False

        elif keep_going:
            print("Failed Month " + month_in_array)
            break


print(picture_to_date(z))
