from datetime import datetime, timedelta

def add_time(start_time, duration_time, start_day=None):
    # Convert start_time to 24-hour format
    start_time_24 = datetime.strptime(start_time, '%I:%M %p')

    # Extract hours and minutes from duration_time
    hours, minutes = map(int, duration_time.split(':'))

    # Create timedelta with the given hours and minutes
    duration_delta = timedelta(hours=hours, minutes=minutes)

    # Add duration_delta to start_time_24
    end_time_24 = start_time_24 + duration_delta

    # Convert the result back to 12-hour format
    end_time = end_time_24.strftime('%I:%M %p')

    # Check if start_day is provided
    if start_day:
        start_day = start_day.lower()
        days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        
        # Find the index of start_day
        start_day_index = days_of_week.index(start_day)

        # Calculate the new day after adding the duration
        end_day_index = (start_day_index + end_time_24.day-1) % 7
        end_day = days_of_week[end_day_index]

        # If it's the next day, append (next day)
        if end_time_24.day-1 == 1:
            end_time += " (next day)"
        elif end_time_24.day > 1:
            end_time += f" ({end_time_24.day-1} days later)"

        # Append the day of the week
        end_time += f", {end_day.capitalize()}"

    return end_time


print(add_time("11:30 PM", "5:25", "Friday"))
