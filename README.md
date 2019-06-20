# Exploring US Bikeshare Data

## Introduction

In this project, I will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. I will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

## Dataset

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

![Text](nyc-data.png)

The Chicago and New York City files also have the following two columns:

- Gender
- Birth Year

The data comes from 3 csv files.

## Project files

- bikeshare.py : Python command line application to analyse data and generate statistics
- chicago.csv : csv file with data for chicago
- new_york_city.csv : csv file with data for new york city
- washington.csv : csv file with data for washington

## Study obectives

For this study, I will aim to compute a variety of descriptive statistics in order to give an overview of the usage of the bike share service:

#### 1. Popular times of travel (i.e., occurs most often in the start time)

- most common month
- most common day of week
- most common hour of day

#### 2. Popular stations and trip

- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

#### 3. Trip duration

- total travel time
- average travel time

#### 4. User info

- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Results
