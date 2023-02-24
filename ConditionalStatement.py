import time
Current_time = time.strftime("%H:%M:%S")
print("The Time is : ", Current_time)
Hours = int(time.strftime("%H"))
print(Hours)
if Hours>=6 and Hours<12:
    print("Good Morning")
elif Hours>12 and Hours<16:
    print("Good Afernoon")
elif Hours>16 and Hours<20:
    print("Good Evening")
else:
    print("Good Night")