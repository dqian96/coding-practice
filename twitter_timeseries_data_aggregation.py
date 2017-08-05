"""
Timeseries Data Aggregation
Input: series of log lines/engagement data from standard input
Output: aggregates the engagement data by month and category
"""

from sys import stdin
from collections import namedtuple, defaultdict

Date = namedtuple('Date', 'year month')
DataPoint = namedtuple('DataPoint', 'date type occurences')

def is_between_dates(inc_lower_bound, exc_upper_bound, date):
    """Tests whether or not a certain date is in [lower_bound, upper_bound) """
    if inc_lower_bound.year == exc_upper_bound.year and \
        date.month >= inc_lower_bound.month and date.month < exc_upper_bound.month:
        return True
    if date.year > inc_lower_bound.year and date.year < inc_lower_bound.year:
        return True
    if date.year == inc_lower_bound.year and date.month >= inc_lower_bound.month:
        return True
    if date.year == exc_upper_bound.year and date.month < exc_upper_bound.month:
        return True
    return False

def time_series_parser(time_series_text):
    """Parses plaintext representing a single data point"""
    tokens = time_series_text.split(",")
    return DataPoint(date_parser(tokens[0].strip()), tokens[1].strip(), int(tokens[2].strip()))

def date_parser(date_text):
    """Parses plaintext representing a date"""
    tokens = date_text.split("-")
    return Date(tokens[0], tokens[1])

def print_records(records):
    """Writes aggregation data/records to standard output from most recent to least"""
    dates = records.keys()
    dates.sort(reverse=True)
    for date in dates:
        concat_list = []        # use .join() on list to prevent string concat
        concat_list.append(date.year + '-' + date.month)
        categories = records[date].keys()
        categories.sort()       # categories in alphabetical order
        for category in categories:
            concat_list.append(category)
            concat_list.append(str(records[date][category]))
        print ", ".join(concat_list)

def main():
    """Main program"""
    records = defaultdict(lambda: defaultdict(int))
    tokens = stdin.readline().split(",")
    lower_bound = date_parser(tokens[0].strip())   # lower and upper temporal bounds
    upper_bound = date_parser(tokens[1].strip())
    stdin.readline()         # discard blank line
    for line in stdin:
        point = time_series_parser(line)
        if is_between_dates(lower_bound, upper_bound, point.date):
            records[point.date][point.type] += point.occurences
    print_records(records)

if __name__ == '__main__':
    main()
