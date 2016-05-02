## testDate.py

from date import Date

def main():
    print('Welcome! This program will tell you the current date and conatins various methods to use on the date')
    today = Date()
    print(today)

    today.setMonth(12)
    print(today)

    today.setDay(5, 4, 2014)
    print(today)
