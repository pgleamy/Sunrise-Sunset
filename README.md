# Sunrise-Sunset Visualization, version 1.0

## Description

Gathers and visualizes data on sunrise and sunset times throughout the year for a given city. The data is gathered from the API provided by sunrise-sunset.org and visualized using matplotlib.

## How to Run

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the main script by typing `python main.py` in your terminal.
4. If running for the first time, you will be prompted to select a city. The city data will be saved and reused for future runs. If you want to visualize a different city, then delete the `city.json` and `collected_sun_data.py` files.
5. The script will collect sunrise and sunset data for the selected city for the current year. This process will take about 8 minutes.
6. Once the data is collected, a visualization will be displayed. You can maximize the visualization and export/save it.

## Example Output

Here is an example of a visualization for Calgary, Alberta:

![Calgary Sunrise-Sunset Visualization](utilities/Calgary-AB-23023.png)

This chart shows the sunrise and sunset times throughout the year. The blue dots represent sunset times, and the orange dots represent sunrise times. The vertical green line represents the current date. The red lines show the changes for daylight savings.

ENJOY!