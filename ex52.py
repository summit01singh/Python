total_sec = int(input("How many seconds, in total?"))
hours = total_sec/3600
sec_still_remaining = total_sec % 3600
minutes = sec_still_remaining / 60
sec_final = sec_still_remaining % 60

print ("Hours =",hours, "Mins =",minutes, "Seconds =",sec_final)
