def test(actual, expected):
    """Compare the actual to the expected value,
        and print a suitable message.
    """
    import sys
    linenum = sys._getframe(1).f_lineno #get the caller's line number.
    if (expected == actual):
        msg = "Test on line {0} passed." .format(linenum)
    else:
        msg = ("Test on line {0} failed. Epected '{1}', but got '{2}'."
                                    .format(linenum, expected, actual))
    print(msg)

def turn_clockwise(dir):
    if (dir == "N"):
        turn = "E"
        return turn
    elif (dir == "W"):
        turn = "N"
        return turn

test (turn_clockwise("W"), "N")
test (turn_clockwise("N"), "E")
test (turn_clockwise("fuck"), "None")

def weekday(num):
    for i in range(6):
        if(num == 0):
            day = 'Sunday'
            return day
        elif(num == 1):
            day = 'Monday'
            return day
        elif(num == 2):
            day = 'Tuesday'
            return day
        elif(num == 3):
            day = 'Wednesday'
            return day
        elif(num == 4):
            day = 'Thursday'
            return day
        elif(num == 5):
            day = 'Friday'
            return day
        elif(num == 6):
            day = 'Saturday'
            return day
        else:
            day = "bye bye"
            return day

test(weekday(0), "Sunday")
test(weekday(3), "Wednesday")
test(weekday(10), "yoo")

def num(weekday):
    #for d in ("Sunday", "Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"):
    if(weekday == "Sunday"):
        number = 0
        return number
    elif(weekday == "Monday"):
        number = 1
        return number
    elif(weekday == "Tuesday"):
        number = 2
        return number
    elif(weekday == "Wednesday"):
        number = 3
        return number
    elif(weekday == "Thursday"):
        number = 4
        return number
    elif(weekday == "Friday"):
        number = 5
        return number
    elif(weekday == "Saturday"):
        number = 6
        return number
    else:
        number = "none"
        return number


test(num("Friday"), 5)
test(num("Sunday"), 0)
test(num("Monday"), 4)

def day_add(day, delta):
    if (delta < 0):
        return weekday((delta % 7))
    elif (delta % 7 == 0):
        return day
    elif (delta % 7 == 1):
        return weekday(1)
    elif (delta % 7 == 2):
        return weekday(2)
    elif (delta % 7 == 3):
        return weekday(3)
    elif (delta % 7 == 4):
        return weekday(4)
    elif (delta % 7 == 5):
        return weekday(5)
    elif (delta % 7 == 6):
        return weekday(6)

test (day_add("Sunday", -1), "Saturday")
test (day_add("Tuesday", -100), "Sunday")
test (day_add("Sunday", -7), "Sunday")

def days_in_month(month):
    if(month == "April"):
        day = 30
        return day
    elif(month == "January"):
        day = 31
        return day


test(days_in_month("February"), 28)
test(days_in_month("January"), 31)
test(days_in_month("April"), 30)

def to_sec(hr, min, sec):
    total_sec = ((hr * 3600) + (min * 60) + sec)
    return int(total_sec)

test(to_sec(2, 30, 10), 9010)
test(to_sec(2, 0, 0), 7200)
test(to_sec(2.5, 0, 10.71), 9010)
