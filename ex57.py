def weekday(num):
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

day_you_leave = (input("Please enter the number between 0-6:-"))
day_you_stay = input("Please enter the number of days you stay:-")
day_you_return = day_you_stay % day_you_leave

print ("you will return on", weekday(day_you_return))
