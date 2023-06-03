import requests
import time
from datetime import date, timedelta

# Latitude and longitude for Calgary, Alberta
lat = 51.0447
lng = -114.0719

# Start and end dates for the year
start_date = date(2023, 1, 1)
end_date = date(2023, 12, 31)

# Number of days in the year
delta = end_date - start_date

sun_dict = {}

for i in range(delta.days + 1):
    day = start_date + timedelta(days=i)
    response = requests.get(f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&date={day.isoformat()}&formatted=0')
    data = response.json()

    if data['status'] == 'OK':
        sun_dict[day.isoformat()] = data['results']
    
    # Wait for 2 seconds before making the next API call
    time.sleep(2)

# Write the dictionary to a Python file
with open('sun_data.py', 'w') as file:
    file.write("# This file contains sunrise and sunset data for Calgary, Alberta for the year 2023\n")
    file.write("sun_data = ")
    file.write(str(sun_dict))
