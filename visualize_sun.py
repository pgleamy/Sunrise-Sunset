from dateutil.parser import parse
from dateutil.tz import gettz
from matplotlib.ticker import FuncFormatter
from dateutil.relativedelta import relativedelta, SU
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def visualize_sunrise_sunset(city, country, lat, lng):
    
    # Import sun_data.py. Is here because it is not possible to import a file that is created during runtime
    from DATA.sun_data import sun_data
    
    # Convert time strings to datetime objects
    def time_to_datetime(time_str):
        return parse(time_str)

    # Convert datetime object to minutes past midnight in local timezone
    def time_to_minutes(time_obj):
        return time_obj.hour * 60 + time_obj.minute + time_obj.second / 60
        
    # Create lists for dates and sun positions
    data_items = list(sun_data.items())
    data_items.sort()  # Sort by date

    dates = []
    sunrise_times = []
    sunset_times = []

    for date_str, sun_info in data_items:
        # Skip the day if sunrise or sunset time is not available
        if 'sunrise' not in sun_info or 'sunset' not in sun_info:
            continue

    for date_str, sun_info in data_items:
        dates.append(parse(date_str))
        sunrise_time = time_to_minutes(time_to_datetime(sun_info['sunrise']))
        sunset_time = time_to_minutes(time_to_datetime(sun_info['sunset']))
        sunrise_times.append(sunrise_time)
        sunset_times.append(sunset_time)

    # Plot sunrise and sunset times
    plt.scatter(dates, sunset_times, color='blue', label='Sunset', s=2)
    plt.scatter(dates, sunrise_times, color='orange', label='Sunrise', s=2)

    # Set the y-axis to display times in 24-hour format
    def format_func(value, tick_number):
        hours = int(value // 60)
        minutes = int(value % 60)
        return f"{hours}:{minutes:02d}"

    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_func))
    plt.gca().set_yticks([i * 60 for i in range(24)])  # Set y-ticks every hour

    # Set the x-axis to display the names of each month
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

    # Add vertical lines for daylight saving time changes
    dst_start = datetime(datetime.now().year, 3, 1) + relativedelta(weekday=SU(2))  # Second Sunday in March
    dst_end = datetime(datetime.now().year, 11, 1) + relativedelta(weekday=SU(1))  # First Sunday in November
    plt.axvline(x=dst_start, color='r', linestyle='--', label='DST Start')
    plt.axvline(x=dst_end, color='r', linestyle='--', label='DST End')

    # Add a vertical line for the current date
    plt.axvline(x=datetime.now(), color='g', linestyle=':', label='Today')

    plt.xlabel('Date')
    plt.ylabel('Time of Day')
    plt.title(f'Sunrise and Sunset Times in {city}, {country} for {datetime.now().year}')
    plt.legend()
    plt.show()
