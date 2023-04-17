# Explore US Bikeshare Data
My first python project of Udacity

## Project Details
In this preject, you will see how to check the Data from the _Bicycle-Sharing systems_ of USA

## The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

```
Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)
```
The Chicago and New York City files also have the following two columns:
```
Gender
Birth Year
```

[Data for the first 10 rides in the new_york_city.csv file](https://video.udacity-data.com/topher/2018/March/5aa771dc_nyc-data/nyc-data.png)

The original files are much larger and messier, and you don't need to download them, but they can be accessed here if you'd like to see them ([Chicago](https://www.divvybikes.com/system-data), [New York City](https://www.citibikenyc.com/system-data), [Washington](https://www.capitalbikeshare.com/system-data)). 
These files had more columns and they differed in format in many cases. Some data wrangling has been performed to condense these files to the above core six columns.

## Statistics Computed:

1. Popular times of travel (i.e., occurs most often in the start time)

    - most common month
    - most common day of week
    - most common hour of day

2. Popular stations and trip

    - most common start station
    - most common end station
    - most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration

    - total travel time
    - average travel time

4. User info

    - counts of each user type
    - counts of each gender (only available for NYC and Chicago)
    - earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Software Needs

You should have Python 3, Numpy and Pandas to run this project

## Udacity data analyst Bikeshare data

This project explores Bike share data from 3 differents cities; it uses data from csv files to compute staticts from those 3 cities, also takes user inputs to create an interactive experience.

## Built with

    - Python
    - Pandas
    - Numpy
    - Pycharm (IDE)

## Dataset Files

    - chicago.csv
    - new_york_city.csv
    - washington.csv
