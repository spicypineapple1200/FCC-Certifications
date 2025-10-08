from datetime import datetime, timedelta

def add_time(start, duration, day=None):

    # Code for getting new time
    time_format = "%I:%M %p"
    initial_time = datetime.strptime(start, time_format)
    
    hours = int(duration.split(":")[0])
    minutes = int(duration.split(":")[1])
    days = str((hours+minutes)/24)
    
    duration_to_add = timedelta(hours=hours, minutes=minutes)
    final_time = initial_time + duration_to_add
    f = [item for item in final_time.strftime(time_format)]
    answer = ""
    for item in f: answer+=item
    if answer[0] == "0":
        answer = answer[1:]

    # Code for getting new day of the week
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day:
        day = day.lower()
        if day not in week_days:
            pass
        else:
            index = week_days.index(day)
            for num in range(int(float(days))):
                index+=1
                if index == 7:
                    index = 0
            new_day = week_days[index]
            answer+=", "+new_day.title()

    # Code for getting days later bit
    print(days)
    if float(days) > 1.0:
        add = int(days.split(".")[0])+1
        day_statement = f"({add} days later)"
        answer+=" "+day_statement
    elif float(days) > 0.99:
        day_statement = "(next day)"
        answer+=" "+day_statement
    else:
        pass
    
    
    print(answer)

add_time('3:30 PM', '2:12', 'Monday')
# should return '5:42 PM, Monday'.

add_time('8:16 PM', '466:02', 'tuesday')
# should return '6:18 AM, Monday (20 days later)'.
