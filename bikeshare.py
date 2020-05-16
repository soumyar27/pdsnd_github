import time
import pandas as pd
import numpy as np

# set option to display all columns and rows on the terminal
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Ask user to input name of the city. Input should be either 'chicago', 'new york city' or 'washington'.
    city = input ("\nEnter name of the city to analyze (Chicago, New York City or Washington): ")
    city = city.title()
    i = 1

    while city not in ('Chicago', 'New York City', 'Washington'):
        city = input ("\nEnter name of the city to analyze (Chicago, New York City or Washington): ")
        city = city.title()
        # Return error message for 5 incorrect inputs
        i = i + 1
        if i == 5 and city not in ('Chicago', 'New York City', 'Washington'):
            print ('\nToo many incorrect inputs')
            exit()

    # Display back the input to the users
    if city in ('Chicago', 'New York City', 'Washington'):
        print('\nYou selected {} for data analysis'.format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    # Ask user to input month. Input should be either 'all', 'january', 'february', 'march', 'april', 'may' or 'june'.
    month = input ("\nEnter month for data analysis (All, January, February, March, April, May or June): ")
    month = month.title()
    i = 1

    while month not in ('All', 'January', 'February', 'March', 'April', 'May', 'June'):
        month = input ("\nEnter month for data analysis (All, January, February, March, April, May or June): ")
        month = month.title()
        # Return error message for 5 incorrect inputs
        i = i + 1
        if i == 5 and month not in ('All', 'January', 'February', 'March', 'April', 'May', 'June'):
            print ('\nToo many incorrect inputs')
            exit()

    # Display back the input to the users
    if month in ('January', 'February', 'March', 'April', 'May', 'June'):
        print('\nYou selected {} for data analysis'.format(month))
    elif month == 'All':
        print('\nYou selected all months for data analysis')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Ask user to input day of the week. Input should be either 'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' or 'sunday'.
    day = input ("\nEnter day of the week for data analysis (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday): ")
    day = day.title()
    i = 1

    while day not in ('All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
        day = input ("\nEnter day of the week for data analysis (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday): ")
        day = day.title()
        # Return error message for 5 incorrect inputs
        i = i + 1
        if i == 5 and day not in ('All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
            print ('\nToo many incorrect inputs')
            exit()

    # Display back the input to the users
    if day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
        print('\nYou selected {} for data analysis'.format(day))
    elif day == 'All':
        print('\nYou selected all days for data analysis')

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
    # load data frame for input city
    df = pd.read_csv(CITY_DATA[city])

    # convert start time into date time format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and weekday of start time into additional columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # for specific month input, filter the data frame with data for that month
    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    # for specific day input, filter the data frame with data for that day
    if day != 'All':
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = days.index(day)

        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most common times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # load month name into month column
    df['month'] = df['Start Time'].dt.month_name()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Start Month: ', common_month)

    # TO DO: display the most common day of week
    # load day of the week name into 'day' column
    df['day'] = df['Start Time'].dt.day_name()

    # print most common start day
    common_day = df['day'].mode()[0]
    print('Most Common Start Day: ', common_day)

    # TO DO: display the most common start hour
    # load start time hour into 'hour' column
    df['hour'] = df['Start Time'].dt.strftime('%I %p')

    # print most common start time hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # print most common start station for the bike trips
    start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station: ',start_station)

    # TO DO: display most commonly used end station
    # print most common end station for the bike trips
    end_station = df['End Station'].mode()[0]
    print('Most Popular End Station: ',end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # print most common combination of start and end stations
    common_trip = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
    trip_start, trip_end = common_trip.index[0]
    print("Most Popular Trip was from \'{}\' to \'{}\'".format(trip_start, trip_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # calculate and display total travel time
    duration = round(df['Trip Duration'].sum())
    hours = duration//3600
    remainder = duration%3600
    minutes = remainder//60
    seconds = remainder%60
    print('Total trip duration: {} hours {} minutes and {} seconds'.format(hours,minutes,seconds))

    # TO DO: display mean travel time
    duration = round(df['Trip Duration'].mean())
    hours = duration//3600
    remainder = duration%3600
    minutes = remainder//60
    seconds = remainder%60
    print('Average trip duration: {} hours {} minutes and {} seconds'.format(hours,minutes,seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # display count of user types
    print('Count of users by type: \n',df['User Type'].value_counts(),'\n')

    # TO DO: Display counts of gender
    # display user count by gender for chicago and new new york
    if len(df.columns) == 11:
        print('There\'s no gender data for washington')
    else:
        df['Gender'] = df['Gender'].dropna()
        print('Count of users by gender: \n',df['Gender'].value_counts(),'\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    # display earliest, most recent and most common birth years for chicago and new york
    if len(df.columns) == 11:
        print('There\'s no birth year data for washington')
    else:
        df['Birth Year'] = df['Birth Year'].dropna()
        print('Earliest birth year: ', int(df['Birth Year'].min()))
        print('Most recent birth year: ', int(df['Birth Year'].max()))
        print('Most common birth year: ', int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """
    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`

    """
    # set a counter variable
    i = 0

    # check if counter is less than or equal to maximum number of rows in the dataframe
    while i < len(df.index):
        # ask if user wants to see 5 lines of raw data
        view_data = input('\nWould you like to see 5 lines of raw data? Enter Y or N: ')
        # set counter for invalid inputs
        x = 1
        # ask user for valid inputs 5 times, else exit out of the function
        while view_data.upper() not in ('Y','N'):
            if x < 5:
                print('\nThat was an invalid input')
                view_data = input('\nWould you like to see 5 lines of raw data? Enter Y or N: ')
                x = x + 1
            else:
                print('\nToo many invalid inputs. Exiting analysis for the current set of filters.')
                return
        # display 5 lines of raw data if user wants to see it
        if view_data.upper() == 'Y':
            print('\n',df.iloc[i:i+5, :])
            i = i + 5
        # exit out of the function when user doesn't want to see raw data
        else:
            print('\nThanks, exiting analysis for the current set of filters')
            return

    # print a message if all available raw data lines have been displayed
    print ('\nThat was all the raw data for the current set of filters')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
