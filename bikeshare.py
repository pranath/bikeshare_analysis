import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please enter a city (from chicago, new york city, washington: ").lower()
    while city not in {'chicago', 'new york city', 'washington'}:
        print("I'm sorry i did'nt recognise that city!")
        city = input("Please enter a city (from chicago, new york city, washington): ").lower()


    # get user input for month (all, january, february, ... , june)
    month = input("Please enter a month (from all, january, february, march, april, may, june): ").lower()
    while month not in {'all', 'january', 'february', 'march', 'april', 'may', 'june'}:
        print("I'm sorry i did'nt recognise that month!")
        month = input("Please enter a city (from january, february, march, april, may, june): ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter a day (from all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ").lower()
    while day not in {'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}:
        print("I'm sorry i did'nt recognise that day!")
        day = input("Please enter a day (from all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ").lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel for bikes are...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month for travel is: ' + datetime.date(1900, most_common_month, 1).strftime('%B') + '\n')

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common week day for travel is: ' + str(most_common_day) + '\n')

    # display the most common start hour
    most_common_hour_start = df['hour'].mode()[0]
    print('The most common hour for starting travel is: ' + str(most_common_hour_start) + ':00 Hrs\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_ss = df['Start Station'].mode()[0]
    print('The most common start station is: ' + most_common_ss + '\n')

    # display most commonly used end station
    most_common_es = df['End Station'].mode()[0]
    print('The most common end station is: ' + most_common_es + '\n')

    # display most frequent combination of start station and end station trip
    df['Start & End Station'] = df['Start Station'] + ' -> ' + df['End Station']
    most_common_ss_es = df['Start & End Station'].mode()[0]
    print('The most common start and end station combination is: ' + most_common_ss_es + '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time_seconds = df['Trip Duration'].sum()
    total_travel_time_years = round(total_travel_time_seconds / 60 /60 / 24 / 365, 2)
    print('The total travel time is: ' + str(total_travel_time_seconds) + ' seconds or ' + str(total_travel_time_years) + ' years\n')

    # display mean travel time
    mean_travel_time_seconds = round(df['Trip Duration'].mean(), 2)
    mean_travel_time_minutes = round(mean_travel_time_seconds / 60, 2)
    print('The mean travel time is: ' + str(mean_travel_time_seconds) + ' seconds or ' + str(mean_travel_time_minutes) + ' minutes\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The number of users of each type are the following: \n')
    print(user_types)

    if city != 'washington':
        print('\n')
        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print('The number of users of each gender are the following: \n')
        print(gender_counts)

        # Display earliest, most recent, and most common year of birth
        earliest_yob = df['Birth Year'].min()
        print('\nThe earliest year of birth is: ' + str(int(earliest_yob)) + '\n')
        latest_yob = df['Birth Year'].max()
        print('The most recent year of birth is: ' + str(int(latest_yob)) + '\n')
        mostcommon_yob = df['Birth Year'].mode()[0]
        print('The most common year of birth is: ' + str(int(mostcommon_yob)) + '\n')

    else:
        print('Gender & birth stats are not available for Washington \n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        start_row = 0
        end_row = 5
        raw_data = input('\nWould you like to view the first 5 rows of data ? Enter yes or no.\n').lower()
        while raw_data != 'no':
            print(df[start_row:end_row])
            start_row += 5
            end_row += 5
            raw_data = input('\nWould you like to view the next 5 rows of data ? Enter yes or no.\n').lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
