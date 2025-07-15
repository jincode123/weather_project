import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # Parse the ISO date string
    date_obj = datetime.fromisoformat(iso_string)
    # Format the date as 'Weekday DD Month YYYY'
    # print(date_obj.strftime("%A %d %B %Y"))
    return (date_obj.strftime("%A %d %B %Y"))

date = "2021-07-05T07:00:00+08:00"
convert_date(date)
result = convert_date(date)
print(result)

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp = float(temp_in_fahrenheit)
    celsius = (temp - 32) * 5 / 9
    if celsius < 0:
        return round(celsius, 1)
    if celsius.is_integer():
        return round(celsius, 1)
    return round(celsius, 1)

temp_in_f = "77"
convert_f_to_c(temp_in_f)
result = convert_f_to_c(temp_in_f)
print(result)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    # Determine input type
    if not weather_data:
        return 0
    is_string = all(isinstance(x, str) for x in weather_data)
    is_negative = all(float(x) < 0 for x in weather_data)
    is_float = any(isinstance(x, float) for x in weather_data)
    numbers = [float(x) for x in weather_data]
    mean = sum(numbers) / len(numbers)
    # Whole number
    if mean.is_integer():
        return int(mean)
    # If input is all strings or all negative, round to 1 decimal
    if is_string or is_negative:
        return round(mean, 1)
    # If any input is float, round to 5 decimals
    if is_float:
        return round(mean, 5)
    # Default: return float
    return mean


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row and len(row) == 3:
                data.append([row[0], int(row[1]), int(row[2])])
    return data
    

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    
    min_value = float('inf')
    min_index = -1
    
    for index, value in enumerate(weather_data):
        value = float(value)  # Ensure the value is a float
        if value <= min_value:
            min_value = value
            min_index = index
            
    return (min_value, min_index)

temperatures = [49, 57, 56, 55, 53]
find_min(temperatures)
result = find_min(temperatures)
print(result)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    
    max_value = float('-inf')
    max_index = -1
    
    for index, value in enumerate(weather_data):
        value = float(value)  # Ensure the value is a float
        if value >= max_value:
            max_value = value
            max_index = index
            
    return (max_value, max_index)

temperatures = [49, 57, 56, 55, 53]
find_max(temperatures)
result = find_max(temperatures)
print(result)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
        return "No data available."

    # Get dates and temperatures
    dates = [convert_date(row[0]) for row in weather_data]
    min_temps = [round(convert_f_to_c(row[1]), 1) for row in weather_data]
    max_temps = [round(convert_f_to_c(row[2]), 1) for row in weather_data]

    # Calculate min/max temperatures and their indexes
    min_temp, min_index = find_min(min_temps)
    max_temp, max_index = find_max(max_temps)

    # Calculate the mean temperatures
    mean_min_temp = round(calculate_mean(min_temps), 1)
    mean_max_temp = round(calculate_mean(max_temps), 1)

    # Round the temperatures and averages to 2 decimal places
    min_temp = round(min_temp, 1)
    max_temp = round(max_temp, 1)
    mean_min_temp = round(mean_min_temp, 1)
    mean_max_temp = round(mean_max_temp, 1)

    # Use a formatting function to output temperatures with 2 decimal places
    def format_temp(temp):
        return "{:.1f}{}".format(float(temp), DEGREE_SYMBOL)

    # Prepare summary lines
    lines = [
        f"{len(weather_data)} Day Overview",
        f"  The lowest temperature will be {format_temp(min_temp)}, and will occur on {dates[min_index]}.",
        f"  The highest temperature will be {format_temp(max_temp)}, and will occur on {dates[max_index]}.",
        f"  The average low this week is {format_temp(mean_min_temp)}.",
        f"  The average high this week is {format_temp(mean_max_temp)}."
    ]
    return "\n".join(lines) + "\n"

example_one = [
            ["2021-07-02T07:00:00+08:00", 49, 67],
            ["2021-07-03T07:00:00+08:00", 57, 68],
            ["2021-07-04T07:00:00+08:00", 56, 62],
            ["2021-07-05T07:00:00+08:00", 55, 61],
            ["2021-07-06T07:00:00+08:00", 53, 62]
        ]
generate_summary(example_one)
result = generate_summary(example_one)
print(result)


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    if not weather_data:
        return "No data available."

    summary_lines = []
    for row in weather_data:
        date = convert_date(row[0])
        min_c = convert_f_to_c(row[1])
        max_c = convert_f_to_c(row[2])
        line = (
            f"---- {date} ----\n"
            f"  Minimum Temperature: {min_c:.1f}{DEGREE_SYMBOL}\n"
            f"  Maximum Temperature: {max_c:.1f}{DEGREE_SYMBOL}"
        )
        summary_lines.append(line)

    # Join lines with two newlines between each, but no newline at the end
    return "\n\n".join(summary_lines)+"\n\n"

example_three = [
            ["2020-06-19T07:00:00+08:00", -47, -46],
            ["2020-06-20T07:00:00+08:00", -51, 67],
            ["2020-06-21T07:00:00+08:00", 58, 72],
            ["2020-06-22T07:00:00+08:00", 59, 71],
            ["2020-06-23T07:00:00+08:00", -52, 71],
            ["2020-06-24T07:00:00+08:00", 52, 67],
            ["2020-06-25T07:00:00+08:00", -48, 66],
            ["2020-06-26T07:00:00+08:00", 53, 66]
        ]

generate_daily_summary(example_three)
result = generate_daily_summary(example_three)
print(result)    