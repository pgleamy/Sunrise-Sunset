import os
import json
import importlib.util
from fuzzywuzzy import process

from select_city import select_city 
from collect_sun_data import collect_sun_data
from visualize_sun import visualize_sunrise_sunset

def main():
    
    # Check if city.json exists
    if not os.path.exists('city.json'):
        # If city.json does not exist, select city
        city = select_city()
        
        # Convert city data to dictionary
        city_dict = {
            "name": city[0],
            "country": city[1],
            "longitude": city[2],
            "latitude": city[3]
        }

        # Define latitude and longitude
        latitude = city_dict["latitude"]
        longitude = city_dict["longitude"]
        
        # Save city to file called city.json
        with open('city.json', 'w', encoding='utf-8') as f:
            json.dump(city_dict, f, ensure_ascii=False, indent=4)
    else:
        # Load city data from city.json
        with open('city.json', 'r') as f:
            city_data = json.load(f)

        # Access the elements of the dictionary
        city_name = city_data["name"]
        country = city_data["country"]
        longitude = city_data["longitude"]
        latitude = city_data["latitude"]
        
        print(f"\nLoaded {city_name}, {country} from city.json. To change City delete city.json and sun_data.py and run this program again.\n")
    
    # Get sun data for the City from sunrise_sunset.org if it hasn't already been collected
    if not os.path.exists('sun_data.py'):
        collect_sun_data(latitude, longitude)
        
    # Load the visualisation module
    visualize_sunrise_sunset(city_name, country, latitude, longitude)
    
if __name__ == '__main__':
    main()

