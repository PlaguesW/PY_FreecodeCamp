def add_time(start, duration, start_day=None):

    time_part, period = start.split()  # Extract start time and period (am/pm)
    start_hour_str, start_minute_str = time_part.split(":")
    start_hour = int(start_hour_str)
    start_minute = int(start_minute_str)

    if period.upper() == "AM":  # Convert start time to 24-hour format
        if start_hour == 12:
            start_hour_24 = 0
        else:
            start_hour_24 = start_hour
    else:
        if start_hour == 12:
            start_hour_24 = 12
        else:
            start_hour_24 = start_hour + 12

    start_total_minutes = start_hour_24 * 60 + start_minute

    dur_hour_str, dur_minute_str = duration.split(":")  # Set duration
    dur_hour = int(dur_hour_str)
    dur_minute = int(dur_minute_str)
    duration_total_minutes = dur_hour * 60 + dur_minute

    # Multiple start minutes with duration minutes
    total_end_minutes = start_total_minutes + duration_total_minutes

    # Calcilate how many days passed
    days_passed = total_end_minutes // (24 * 60)

    # Determine the final within one day ( hours and minutes )
    end_minutes_of_day = total_end_minutes % (24 * 60)
    end_hour_24 = end_minutes_of_day // 60
    end_minute = end_minutes_of_day % 60

    if end_hour_24 == 0:  # Convert form 24h format into 12h
        end_hour_12 = 12
        end_period = "AM"

    elif end_hour_24 == 12:
        end_hour_12 = 12
        end_period = "PM"

    elif end_hour_24 < 12:
        end_hour_12 = end_hour_24
        end_period = "AM"

    else:
        end_hour_12 = end_hour_24 - 12
        end_period = "PM"

    #  Format time: Hour( without leading zero ); Min( with leading zero ) AM/PM
    new_time_str = f"{end_hour_12}:{end_minute:02d} {end_period}"

    # If there is a starting day, take it into account
    if start_day:
        days_of_week = ["Monday", "Tuesday", "Wednesday",
                        "Thursday", "Friday", "Saturday", "Sunday"]
        start_day_norm = start_day.capitalize()
        start_day_index = days_of_week.index(start_day_norm)
        end_day_index = (start_day_index + days_passed) % 7
        end_day = days_of_week[end_day_index]
        new_time_str += f", {end_day}"

    if days_passed == 1:
        new_time_str += " (next day)"
    elif days_passed > 1:
        new_time_str += f" ({days_passed} days later)"

    return new_time_str
