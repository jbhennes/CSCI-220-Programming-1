## test Date.

from date import Date

def main():
    today = Date()
    print(today)

    print('\nTesting setMonth()')
    today.setMonth(-4)
    print(today)
    today.setMonth(13)
    print(today)
    today.setMonth(4.5)
    print(today)
    today.setMonth(4)
    print(today)

    print('\nTesting setYear()')
    today.setYear(2014.5)
    print(today)
    today.setYear(1581)
    print(today)
    today.setYear(-2)
    print(today)
    today.setYear(2014)
    print(today)

    print('\nTesting setDay()')
    today.setDay(31)
    print(today)
    today.setDay(-1)
    print(today)
    today.setDay(15.3)
    print(today)
    today.setDay(14)
    print(today)

main()
