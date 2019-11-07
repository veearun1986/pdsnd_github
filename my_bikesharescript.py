import time
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

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('\nWhich city you want to explore chicago, new york city or washington!! Know some cool trivia!\n')
        city = city.lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('Please input city name as mentioned(lower case)''-->''chicago, new york city or washington')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month do you want to look for? january, february, march, april, may, june or all?\n')
        month = month.lower()
        if month not in ['january','february','march','april','may','june','all']:
            print('Please input month name as mentioned(lower case)''-->''january, february, march, april, may, june, all')
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich day of month do you want to look for? monday, tuesday, wednesday, thursday, friday, saturday, sunday or all?\n')
        day = day.lower()
        if day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
            print('Please input the day as mentioned(lower Case)''-->''monday, tuesday, wednesday, thursday, friday, saturday, sunday, all')
            continue
        else:
            break

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
    # load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day from Start Time for new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        month_name = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month_name.index(month) + 1

    	# filter by month to create new dataframe
        df = df[df['month'] == month]

        # filter by day
    if day != 'all':
        # filter by day to create new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is :', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of week is :', common_day)

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    start_hour = df['start_hour'].mode()[0]
    print('The most common start hour is:', start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode().to_string(index = False)
    print('The most commonly used start station is : {}'.format(common_start))

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode().to_string(index = False)
    print('The most commonly used end station is : {}'.format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    Combo_Station = df.groupby(['Start Station', 'End Station']).count()
    print('The most frequent combination of start and end station trip is :', common_start, " and ", common_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    year, day = divmod(day, 365)
    print('The total travel time is : {} years, {} days, {} hours, {} minutes, {} seconds'.format(year, day, hour, minute, second))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    minut, sec = divmod(mean_travel_time, 60)
    print('The mean travel time is : {} minutes, {} seconds'.format(minut, sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        count_user_type = df['User Type'].value_counts()
        print('\nBelow are the users & their count:\n', count_user_type)
    except KeyError:
        print('\nuser types not available for this month:\n')

    # TO DO: Display counts of gender
    try:
        count_gender = df['Gender'].value_counts()
        print('\nBelow is the Gender split & their count:\n', count_gender)
    except KeyError:
        print('\ngender types not available for this month:\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        print('\nEarliest Birth Year:', earliest)
    except KeyError:
        print("\nEarliest Birth Year:\nData not available.")

    most_recent = int(df['Birth Year'].max())
    print('The most recent year of when someone born is :\n', most_recent)

    common_year = int(df['Birth Year'].mode())
    print('The most common year when people were born is :\n', common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    """print 5 rows at a time and wait for user inputs."""
    idx = 0
    five_data = input("\nWould you like to see 5 rows of data? 'yes' or 'no' \n")
    five_data = five_data.lower()
    while True:
        if five_data == 'no':
            return
        if five_data == 'yes':
            print(df[idx: idx + 5])
            idx = idx + 5
        five_data = input("\nWould you like to see next five rows of data? 'yes' or 'no' \n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
