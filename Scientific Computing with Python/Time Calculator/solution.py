def add_time(start, duration, day=None):
    
    # Time Calculations
    end_bit = start.split(" ")[1]
    new_time = start.split(" ")[0]
    nt1 = int(new_time.split(":")[0])+int(duration.split(":")[0])
    nt2 = int(new_time.split(":")[1])+int(duration.split(":")[1])
    days_passed = 0
    while nt2 >= 60:
        nt2-=60
        nt1+=1
    while nt1 >= 12:
        nt1-=12
        if end_bit == "AM": end_bit = "PM"
        else: 
            end_bit = "AM"
            days_passed+=1
    if len(str(nt2)) == 1:
        nt2 = str(nt2)
        nt2 = '0' + nt2
    nt1 = str(nt1)
    if nt1 == '0': nt1 = '12'
    answer = f"{nt1}:{nt2} {end_bit}"
    
    # Day Calculations
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

    # Final Answers
    print(answer)
    return answer
