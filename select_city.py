import json
import importlib.util
from fuzzywuzzy import process

def get_best_match(city_name, cities):
    # Get the best matches to city_name in cities
    matches = process.extract(city_name, cities, limit=10)
    return matches

# Select city with fuzzy matching. Returns tuple with city name, country, longitude, and latitude.
def select_city():
    # Load cities from cities_sorted.py file
    spec = importlib.util.spec_from_file_location("cities_sorted", "cities_sorted.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    cities = module.Cities

    # Convert all city names to lowercase for case-insensitive matching
    cities_lower = {city['name'].lower(): [] for city in cities}
    for city in cities:
        cities_lower[city['name'].lower()].append(city)

    # Prompt user for city name
    city_name = input('\nEnter the name of the nearest city to you: ')

    # Check if city_name is in cities
    if city_name.lower() in cities_lower:
        city_list = cities_lower[city_name.lower()]
        for i, city in enumerate(city_list, start=1):
            print(f"{i}. {city['name']}, {city['country']}")
        selection = int(input('Enter the number of your choice: '))
        city = city_list[selection-1]
        print(f"City: {city['name']}, Country: {city['country']}, Longitude: {city['lng']}, Latitude: {city['lat']}")
        return city['name'], city['country'], city['lng'], city['lat']
    else:
        # Get the best matches
        matches = get_best_match(city_name, cities_lower.keys())

        if matches:
            print("Did you mean one of these cities?")
            match_cities = []
            for match in matches:
                city_list = cities_lower[match[0]]
                for city in city_list:
                    match_cities.append(city)
            for i, city in enumerate(match_cities, start=1):
                print(f"{i}. {city['name']}, {city['country']}")
            print(f"{i+1}. None of them are right.")
            selection = int(input('Enter the number of your choice: '))
            if selection <= i:
                city = match_cities[selection-1]
                #print(f"City: {city['name']}, Country: {city['country']}, Longitude: {city['lng']}, Latitude: {city['lat']}")
                return city['name'], city['country'], city['lng'], city['lat']
            else:
                print('City not found.')
                return None
        else:
            print('City not found.')
            return None






