# Sunrise and Sunset Times Visualization

This project is a collection of scripts that gather and visualize data on sunrise and sunset times throughout the year. The data is specific to Calgary, Alberta, but future modifications will allow users to input their own location and timezone.

## Project Structure

The project consists of three main parts:

1. **Data Collection Script**: This script collects data on sunrise and sunset times from a reliable source. It runs once a day and updates the data file with the new information.

2. **Data File**: This is a JSON file that stores the collected data. Each entry in the file represents one day and contains the date, sunrise time, and sunset time.

3. **Visualization Script**: This script reads the data from the data file and creates a scatter plot of sunrise and sunset times throughout the year. The x-axis represents the date and the y-axis represents the time of day. The plot also includes vertical lines indicating the start and end of daylight saving time.

## Future Work

In the future, I'll modify the scripts to prompt the user for their location and timezone when collecting the data and save this to a .env file. This will allow the plot to reflect sunrise and sunset times for any location and timezone, not just Calgary, Alberta MST.

## How to Run

To run the data collection script, use the following command:

```bash
python data_collection.py
```

To create the visualization, use the following command:

```bash
python visualization.py
```
