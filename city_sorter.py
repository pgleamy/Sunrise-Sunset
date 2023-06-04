import json
import zipfile

def main():
    # Load cities from zipped JSON file
    with zipfile.ZipFile('cities.zip', 'r') as z:
        with z.open('cities.json') as f:
            cities = json.load(f)

    # Sort cities by name
    cities_sorted = sorted(cities, key=lambda city: city['name'].lower())

    # Save sorted cities to file
    with open('cities_sorted.py', 'w', encoding='utf-8') as f:
        f.write('Cities = [\n')
        for city in cities_sorted:
            f.write(f'    {city},\n')
        f.write(']\n')

if __name__ == '__main__':
    main()

