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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter the city name: ')
    while city not in ["chicago", "new york city", "washington"]:
        city = input("U need to chose between chicago, new york city OR washington: ").lower()

    # get user input for month (all, january, february, ... , june)
    month = input("Enter month: ").lower()
    while month not in ["all", "january", "february", "march", "april", "may", "june"]:
        month = input('U need to chose month between all, january, february, march ,april, may or june : ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("ENTER DAY : ").lower()

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
    # read csv
    df = pd.read_csv(CITY_DATA[city])

    # convert time type and get month from start time
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
    df["Month"] = df["Start Time"].dt.month

    # filter
    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df["Month"] == month]

    # day of the week
    df["day_of_the_week"] = df["Start Time"].dt.day_name()

    # filter by day of week if applicable
    if day != "all":
        df = df[df["day_of_the_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df["Month"].value_counts().idxmax()
    print("The most common month is: ", most_common_month)

    # display the most common day of week
    print("The most common day of week is: ", df["day_of_the_week"].value_counts().idxmax())

    # display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    print("The most common start hour is: ", df["hour"].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common start station is: ", df["Start Station"].value_counts().idxmax())

    # display most commonly used end station
    print("The most common end station is: ", df["End Station"].value_counts().idxmax())

    # display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip:", df.groupby(["Start Station", "End Station"]).size().sort_values(ascending=False).head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("total travel time in second is: ", df["Trip Duration"].sum())

    # display mean travel time

    print("mean travel time in second is: ", df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df["User Type"].value_counts())

    # Display counts of gender
    try:
        print(df["Gender"].value_counts())
    except KeyError:
        print("Didn't catch Gender Information")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birthyear = int(df["Birth Year"].min())
        most_recent_birthyear = int(df["Birth Year"].max())
        most_common_birthyera = int(df["Birth Year"].value_counts().idxmax())
        print("The earliest year of birth is:",earliest_birthyear,
              ", most recent one is:",most_recent_birthyear,
               "and the most common one is: ",most_common_birthyera)
    except KeyError:
        print("Didn't catch Birth Year Information")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw(df):
    """ Your docstring here """
    i = 0
    raw = input("\nDo you want to view the data? Enter yes or no.\n").lower()
    pd.set_option('display.max_columns',200)
    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i: i + 5])  # Display next five rows
            raw = input( "\nWould you like to see 5 more rows of the raw data? "
                    "Type 'Yes' or 'No': ").lower() 
            i += 5 # If yes then display next five rows
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == "no":
            break
        elif restart.lower() != "yes":
            print("Your input is invalid. Please enter only 'yes' or 'no'")
            restart = input('\nWould you like to restart? Enter yes or no.\n')


if __name__ == "__main__":
	main()
