

from sys import stdin
from enum import Enum

class Category(Enum):
    clicks = 1
    app_installs = 2
    favorites = 3
    retweets = 4
    impressions = 5

def isWithin(bounds, date):

def time_series_parser(time_series_text):
    s = time_series_text.split(",")
    return (date_parser(s[0].strip()), Category[s[1].strip()], int(s[2].strip()))


def date_parser(date_text):
    s = date_text.split("-")
    return (int(s[0]), int(s[1]))

def main():
    bounds = map(lambda d: date_parser(d.strip()), stdin.readline().split(","))     # get start and end dates of interest
    stdin.readline()         # blank line
    for line in stdin:
        time_series_parser(line)



if __name__ == '__main__':
    main()