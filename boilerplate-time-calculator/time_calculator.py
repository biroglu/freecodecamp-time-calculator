def add_time(start, duration, today=""):
    minutes = int(start.split()[0][-2:]) + int(duration[-2:])
    hours = int(start.split()[0][:start.index(":")]) + int(duration[:duration.index(":")])
    meridiem = start.split()[1].lower()
    current_day = ""

    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    if today != "":
        current_day = weekdays.index(today.lower())

    if minutes >= 60:
        clock_minutes = minutes - 60
        if clock_minutes < 10:
            clock_minutes = f"{clock_minutes:02}"

        hours += 1
        days_later = hours // 24

        if (hours % 24) > 12 and meridiem == "pm":
            meridiem = "AM"
            days_later += 1
        elif (hours % 24) > 12 and meridiem == "am":
            meridiem = "PM"
        elif (hours % 24) < 12 and meridiem == "pm":
            meridiem = "PM"
        elif (hours % 24) < 12 and meridiem == "am":
            meridiem = "AM"
        elif (hours % 24) == 12 and meridiem == "am":
            meridiem = "PM"
        elif (hours % 24) == 12 and meridiem == "pm":
            meridiem = "AM"
            days_later += 1

        if hours > 12:
            if hours % 12 == 0:
                clock_hour = 12
            else:
                clock_hour = f"{hours % 12}"
        else:
            clock_hour = f"{hours}"
    else:
        clock_minutes = minutes
        if clock_minutes < 10:
            clock_minutes = f"{clock_minutes:02}"

        days_later = hours // 24

        if (hours % 24) > 12 and meridiem == "pm":
            meridiem = "AM"
            days_later += 1
        elif (hours % 24) > 12 and meridiem == "am":
            meridiem = "PM"
        elif (hours % 24) < 12 and meridiem == "pm":
            meridiem = "PM"
        elif (hours % 24) < 12 and meridiem == "am":
            meridiem = "AM"
        elif (hours % 24) == 12 and meridiem == "am":
            meridiem = "PM"
        elif (hours % 24) == 12 and meridiem == "pm":
            meridiem = "AM"
            days_later += 1

        if hours > 12:
            if hours % 12 == 0:
                clock_hour = 12
            else:
                clock_hour = f"{hours % 12}"
        else:
            clock_hour = f"{hours}"

    if days_later == 0 and today == "":
        return f"{clock_hour}:{clock_minutes} {meridiem}"
    elif days_later == 0 and today != "":
        return f"{clock_hour}:{clock_minutes} {meridiem}, {weekdays[(current_day + days_later) % len(weekdays)].capitalize()}"
    elif days_later != 0 and today == "":
        if days_later == 1:
            return f"{clock_hour}:{clock_minutes} {meridiem} (next day)"
        else:
            return f"{clock_hour}:{clock_minutes} {meridiem} ({days_later} days later)"
    elif days_later != 0 and today != "":
        if days_later == 1:
            return f"{clock_hour}:{clock_minutes} {meridiem}, {weekdays[(current_day + days_later) % len(weekdays)].capitalize()} (next day)"
        else:
            return f"{clock_hour}:{clock_minutes} {meridiem}, {weekdays[(current_day + days_later) % len(weekdays)].capitalize()} ({days_later} days later)"


add_time("6:30 PM", "205:12")