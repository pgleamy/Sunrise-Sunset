import requests
import time
from datetime import date, timedelta
from tqdm import tqdm
import os
import json

#Collects sunrise and sunset data for the current year for the given latitude and longitude from the sunrise-sunset.org API. Results in sun_data.py as a dictionary. This takes 5-6 minutes to run because of the API rate limit of 1 call per second.
def collect_sun_data(lat, lng):
    # Get the current year from the OS
    current_year = date.today().year

    # Start and end dates for the year
    start_date = date(current_year, 1, 1)
    end_date = date(current_year, 12, 31)

    # Number of days in the year
    delta = end_date - start_date
    
    # Make a request to the GeoNames Timezone API
    response = requests.get(f"http://api.geonames.org/timezoneJSON?lat={lat}&lng={lng}&sunsetsunrise")

    # Parse the JSON response
    data = json.loads(response.text)

    # The timezone of the location is in data['timezoneId']
    timezone_str = data['timezoneId']
    print(timezone_str)

    sun_dict = {}

    for i in tqdm(range(delta.days + 1), desc="Collecting sun data", ncols=75):
        day = start_date + timedelta(days=i)
        response = requests.get(f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&date={day.isoformat()}&formatted=0')
        data = response.json()

        if data['status'] == 'OK':
            sun_dict[day.isoformat()] = data['results']
        
        # Wait for 1 second before making the next API call to be gentle with the API calls
        time.sleep(1)

    # Write the dictionary to a Python file
    with open('sun_data.py', 'w') as file:
        file.write(f"# This file contains sunrise and sunset data for the location with latitude {lat} and longitude {lng} for the year {current_year}\n")
        file.write("sun_data = ")
        file.write(str(sun_dict))


