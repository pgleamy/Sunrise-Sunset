from datetime import datetime
import pytz
import requests
import json
import importlib.util
import os

def convert_to_local_timezone(utc_datetime_str, timezone_id):
    # Parse the UTC datetime string to a datetime object
    utc_datetime = datetime.strptime(utc_datetime_str, "%Y-%m-%dT%H:%M:%S+00:00")

    # Set the timezone of the datetime object to UTC
    utc_datetime = pytz.utc.localize(utc_datetime)

    # Convert the datetime object to the local timezone
    local_datetime = utc_datetime.astimezone(pytz.timezone(timezone_id))

    return local_datetime

def update_sun_data_with_local_timezone(sun_data, latitude, longitude):
    # Get the timezone ID for the city
    timezone_id = get_time_zone(latitude, longitude)

    # Iterate over all dates in the sun_data dictionary
    for date, data in sun_data.items():
        # Adjust all times to the local timezone
        for key, utc_datetime_str in data.items():
            if isinstance(utc_datetime_str, str) and utc_datetime_str.endswith("+00:00"):
                # Convert the UTC datetime string to a datetime object in the local timezone
                local_datetime = convert_to_local_timezone(utc_datetime_str, timezone_id)

                # Update the time in the sun_data dictionary
                sun_data[date][key] = local_datetime.strftime("%Y-%m-%dT%H:%M:%S%z")

    return sun_data

def get_time_zone(latitude, longitude):
    username = "sunsetsunrise"  # replace with your GeoNames username
    response = requests.get(f"http://api.geonames.org/timezoneJSON?lat={latitude}&lng={longitude}&username={username}")

    data = response.json()
    print(response.text)
    return data.get('timezoneId')


def convert_tz():
    # Define the path to the sun_data.py and city.json files
    sun_data_file_path = os.path.join("DATA", "sun_data.py")
    city_data_file_path = os.path.join("DATA", "city.json")

    # Load the sun_data dictionary from the sun_data.py file
    spec = importlib.util.spec_from_file_location("sun_data", sun_data_file_path)
    sun_data_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sun_data_module)
    sun_data = sun_data_module.sun_data

    # Load the city data from the city.json file
    with open(city_data_file_path, "r") as file:
        city_data = json.load(file)

    # Get the latitude and longitude from the city data
    latitude = city_data['latitude']
    longitude = city_data['longitude']

    # Update the sun_data dictionary with the correct timezone for the location
    sun_data = update_sun_data_with_local_timezone(sun_data, latitude, longitude)

    # Save the updated sun_data dictionary back to the sun_data.py file
    with open(sun_data_file_path, "w") as file:
        file.write("sun_data = " + json.dumps(sun_data, indent=4))

