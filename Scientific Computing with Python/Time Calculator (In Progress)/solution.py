def add_time(start, duration, day=None):
    end_bit = start.split(" ")[1]
    new_time = start.split(" ")[0]
    nt1 = int(new_time.split(":")[0])+int(duration.split(":")[0])
    nt2 = int(new_time.split(":")[1])+int(duration.split(":")[1])
    print(nt1, nt2)
    days_passed = 0
    while nt2 >= 60:
        nt2-=60
        nt1+=1
    while nt1 > 12:
        nt1-=12
        if end_bit == "AM": end_bit = "PM"
        else: 
            end_bit = "AM"
            days_passed+=1
    answer = f"{nt1}:{nt2} {end_bit}"

    if day:
        day = day.lower()
        week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        num = (week_days.index(day))+days_passed
        while num > 6:
            num-=7
        day = week_days[num].title()
        answer+=f", {day}"
    if days_passed == 1: answer+=" (next day)"
    elif days_passed > 1: answer+=f" ({days_passed} days later)"
    else:pass
    print(answer)

add_time('11:59 PM', '24:05', 'Wednesday')
# should return '12:04 AM, Friday (2 days later)'.
