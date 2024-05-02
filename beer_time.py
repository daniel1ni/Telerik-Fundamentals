time = input() #13:00 PM

if (time[1] == ":" or time[2] == ":") and (time[-3:] == " AM" or time[-3:] == " PM"):
    hour_minutes, time_slot = time.split()
    hour, minutes = hour_minutes.split(":")
    if hour.isdigit() and minutes.isdigit():
        hour = int(hour)
        minutes = int(minutes)
        if (hour >= 0 and hour <13) and (minutes >= 0 and minutes < 60):
            if time_slot == "PM":
                hour += 12
            if 12 <= hour < 24 or hour < 3:
                print("beer time")
            else:
                print("non-beer time")
    else:
        print("invalid time")
else:
        print("invalid time")
