day_dict = {
0: 'Sunday',
1: 'Monday',
2: 'Tuesday',
3: 'Wednesday',
4: 'Thursday',
5: 'Friday',
6: 'Saturday',
}

def day_num_to_day_string(num):
    try:
        return day_dict[num]
    except:
        return "Invalid number provided."
print ("so the day is", day_num_to_day_string(5))
