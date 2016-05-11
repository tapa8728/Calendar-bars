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
 1. **parseRawData( )**
      - Parses the `drinking_answers.txt` file into a nested dictionary `dic`. The key for this dictionary is a custom string of the format `yyyy-mm-dd`(`2015-11-19`). The value for each key is a dictionary composed of following key-value pairs - female, male, day, month, year. The male and female keys each have a dictionary for their values. This dictionary consists of key-value pairs for - no, yes, numyes, total. A simple example for the nested dictionary `{'male': {'total': 4, 'yes': 0, 'numyes': 0, 'no': 4}, 'year': 2015, 'day': 19, 'female': {'total': 11, 'yes': 2, 'numyes': 4, 'no': 9}, 'month': 11}`. `'yes'` stands for number of individuals who did drink on that date, `'numyes'` stands for the number of drinks all the individuals drank on that day, `'no'` stands for the number of individuals who did not drink on that date and `'total'` is the total number of individuals who completed the survey on that day.
      - This dictionary can be iterated over and the average number of drinks per day for men and women can be computed. 
      - While parsing the raw data the value for `year_list` is also computed that contains the years for which data is available.
      
 2. **createAmchartsJSON( )**
    - This function creates a JSON file for each year that is present in `year_list`. 
    - For the year `2015` the `start_date` for data procesing will be 1st April, for the future years it will be 1st January. 
    - For every year, a list of dictionaries `thisYear` is created where each dictionary is of the format `{'date' : 2015-11-19, 'weekday':'Thursday', 'male': 1.06, 'female': 1.2}`. `'male'` stands for the avergae number of drinks had by the males on that day and similarly for `'female'`. 
    - Along with this, for every year blank vallues are updated for the dates starting `tomorrow` till `end_date`. Again for `2015` the dates fom 1st Jan to 31st March are blanked out. This is done so that the months on the timeseries charts are aligned one below the other. 
    - The list `thisYear` is first sorted based on the `'date'` key and dumped to a JSON file names as `timeseries_YYYY.json` for the particular year in question. Thus for each year present in `year_list` a JSON file will be generated. 
    
 3. **daterange( )**
   - This function is used to create a date range given the `start` and `end` dates.   

### Front-end documentation
The **timeseries.html** file contains the HTML, Javascript and CSS code for rendering the graphs. 

## Timeseries Visualization
Yearly mouse-wheel enabled zoomable charts with interactive legend and smooth animation. 

![alt tag](https://github.com/tapa8728/Calendar-bars/blob/master/screenshots/drinking.png)

## Barchart Visualization
For each month of the year on each day to represent the number of average drinks

![alt tag](https://github.com/tapa8728/Calendar-bars/blob/master/screenshots/september.png)







