# Daily Visualization of Drinking Patterns

## Heroku hosting
https://drinking-calendar.herokuapp.com/

## Code Documentation

### File Description
- **Raw data source** : `drinking_answers.txt`
- **Data processing script** : `operation.py`
- **Front-end code** : `timeseries.html`
- **Output files**: `data/timeseries_2015.json`, `data/timeseries_2015.json`

### Data processing documentation
The **operation.py** operates on the raw data file **drinking_answers.txt** and converts it into JSON files that can be used by amcharts to render in a timeseries graphs. The detailed description of the functions is below -
 1. **parseRawData()**
      - parses the `drinking_answers.txt` file into a nested dictionary `dic`. The key for this dictionary is a custom string of the format `yyyy-mm-dd`
      - 
 2. **createAmchartsJSON()**

## Timeseries Visualization
Yearly mouse-wheel enabled zoomable charts with interactive legend and smooth animation. 

![alt tag](https://github.com/tapa8728/Calendar-bars/blob/master/screenshots/drinking.png)

## Barchart Visualization
For each month of the year on each day to represent the number of average drinks

![alt tag](https://github.com/tapa8728/Calendar-bars/blob/master/screenshots/september.png)







