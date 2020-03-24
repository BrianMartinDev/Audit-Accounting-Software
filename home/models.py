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
print()


def picture_to_date(picture):
    # ['Feb', '25,', '10:39', 'pm', "Denny's", 'Deliveries', 'Distance', 'Wait', 'Time', 'Base', 'Bonus',
    # 'Estimated', 'Payout', '1ofi', '2.97', 'mi', '2.14', 'min', '$3.99', '$2.78', '$6.77']

    # Tested fields
    month = ''
    day = '25'
    time = '10:39'
    cycle = ["am", "pm"]
    restaurant = "Denny's"
    mileage = '2.97'
    minutes = '2.14'
    base_pay = '$3.99'
    bonus = '$2.78'
    payout = '$6.77'

    # Month test
    month_index_counter = 0
    month_passed = month
    month_failed = 0
    keep_going = True
    months_array = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

    while keep_going:
        # Month
        for month_passed in months_array:
            if month_passed in picture:
                break  # search through picture and find month

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
            print("Passed Month Result: " + str(month_to_num) + " Expected " + month_passed)
            print("Result converted from: " + month_in_array + " to " + str(month_to_num))
            print("Expected: " + month_passed)
            print()
            keep_going = False

        elif keep_going:
            print("Failed Month Result: " + month_in_array + " Expected " + month_passed)
            print("Result: " + month_in_array)
            print("Expected: " + month_passed)
            print()
            break

    # Day test
    day_passed = day
    day_failed = 0
    keep_going = True

    while keep_going:
        day_failed = day_failed + 1
        print("try # ", month_failed)

        # Get Day from list
        day_to_string = picture[month_index_counter]  # Counter of Month index

        day_to_string = day_to_string.rstrip(',')
        day_to_int = int(day_to_string)

        for day in range(31):
            if day == day_to_int:
                day_to_string_convert = str(day_to_int) + ","
                break

        for days_to_strip in picture:
            if day_to_string_convert == days_to_strip:
                day_to_string_back = day_to_string_convert.rstrip(',')
                break

        if day_to_string_back == day_passed:
            print("Passed Day output")
            print("Result: " + day_to_string_back)
            print("Expected: " + day_passed)
            print()

            keep_going = False

        elif keep_going:
            print("Failed Day output")
            print("Result: " + day_to_string_back)
            print("Expected: " + day_passed)
            print()
            break
    # Day test
    time_passed = time
    day_failed = 0
    keep_going = True
    while keep_going:
        day_failed = day_failed + 1
        print("try # ", month_failed)

        # Get Day from list
        index_of_time = picture[month_index_counter + 1]  # Counter of Month index + 1
        print(index_of_time)

        if index_of_time == time_passed:
            print("Passed Time output")
            print("Result: " + index_of_time)
            print("Expected: " + time_passed)
            print()
            keep_going = False

        elif keep_going:
            print("Failed Time output")
            print("Result: " + index_of_time)
            print("Expected: " + time_passed)
            print()
            break

    # Time of Day test
    time_of_day_passed = cycle
    time_of_day_failed = 0
    keep_going = True

    while keep_going:
        time_of_day_failed = time_of_day_failed + 1
        print("try # ", month_failed)

        # Get Day from list
        index_time_of_day = picture[month_index_counter + 2]  # Counter of Month index + 2
        print(index_time_of_day)
        for time_formatted in time_of_day_passed: time_formatted.islower()

        if index_time_of_day == time_formatted:
            print("Passed Time of day output")
            print("Result: " + index_time_of_day)
            print("Expected: " + time_formatted)
            print()
            keep_going = False

        elif keep_going:
            print("Failed Time of day output")
            print("Result: " + index_time_of_day)
            print("Expected: " + time_formatted)
            print()
            break

    restaurant_name = restaurant
    restaurant_test_failed = 0
    keep_going = True

    while keep_going:
        restaurant_test_failed = restaurant_test_failed + 1
        print("try # ", restaurant_test_failed)

        index_of_restaurant = picture[month_index_counter + 3]
        print(index_of_restaurant)

        for x in picture[4:len(picture)]:
            if x == 'Deliveries':
                break

        if index_of_restaurant == restaurant_name:
            print("Passed name of restaurant test output")
            print("Result: " + index_of_restaurant)
            print("Expected: " + restaurant_name)
            print()
            keep_going = False

        elif keep_going:
            print("Failed name of restaurant")
            print("Result: " + index_of_restaurant)
            print("Expected: " + restaurant_name)
            print()

    mileage_test = mileage
    mileage_test_failed = 0
    keep_going = True

    while keep_going:
        mileage_test_failed = mileage_test_failed + 1
        print("try # ", mileage_test_failed)

        miles_index = picture.index('mi')
        print(type(picture[miles_index - 1]))

        miles = picture[miles_index - 1]

        if miles == mileage_test:
            print("Passed mileage")
            print("Result: " + miles)
            print("Expected: " + mileage_test)
            print()
            keep_going = False

        elif keep_going:
            print("Failed mileage")
            print("Result: " + miles)
            print("Expected: " + mileage_test)
            print()

    minutes_test = minutes
    minutes_test_failed = 0
    keep_going = True

    while keep_going:
        minutes_test_failed = minutes_test_failed + 1
        print("try # ", restaurant_test_failed)

        minutes_index = picture.index('min')
        print(type(picture[minutes_index - 1]))
        minutes = picture[minutes_index - 1]

        if minutes == minutes_test:
            print("Passed minutes")
            print("Result: " + minutes)
            print("Expected: " + minutes_test)
            print()
            keep_going = False

        elif keep_going:
            print("Failed minutes")
            print("Result: " + minutes)
            print("Expected: " + minutes_test)
            print()

    base_test = base_pay
    base_pay_test_failed = 0
    keep_going = True

    while keep_going:
        base_pay_test_failed = base_pay_test_failed + 1
        print("try # ", base_pay_test_failed)

        base_pay = picture[-3]
        if base_pay.startswith('$'):
            print(base_pay)

        if base_pay == base_test:
            print("Passed base")
            print("Result: " + base_pay)
            print("Expected: " + base_test)
            print()
            keep_going = False

        elif keep_going:
            print("Failed base")
            print("Result: " + base_pay)
            print("Expected: " + base_test)
            print()

    bonus_test = bonus
    bonus_test_failed = 0
    keep_going = True

    while keep_going:
        bonus_test_failed = bonus_test_failed + 1
        print("try # ", bonus_test_failed)

        bonus_pay = picture[-2]
        if bonus_pay.startswith('$'):
            print(bonus_pay)

        if bonus_pay == bonus_test:
            print("Passed bonus")
            print("Result: " + bonus_pay)
            print("Expected: " + bonus_test)
            print()
            keep_going = False

        elif keep_going:
            print("Failed bonus")
            print("Result: " + bonus_pay)
            print("Expected: " + bonus_test)
            print()

    payout_test = payout
    payout_test_failed = 0
    keep_going = True

    while keep_going:
        payout_test_failed = payout_test_failed + 1
        print("try # ", payout_test_failed)

        payout = picture[-1]
        if payout.startswith('$'):
            print(payout)

        if payout == payout_test:
            print("Passed payout")
            print("Result: " + payout)
            print("Expected: " + payout)
            keep_going = False

        elif keep_going:
            print("Failed payout")
            print("Result: " + payout)
            print("Expected: " + payout_test)
            print()

print(picture_to_date(z))
print("Time ""| Restaurant | Distance | Wait | Base | Bonus | payout")
