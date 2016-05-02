# sum.py

def main():
    print "This program will ask how many numbers the user will enter."
    print "Then it asks for the numbers and adds them up."

    count = input("How many numbers do you want to add? ")
    sum = 0

    for i in range(count):
        number = input("Enter a number: ")
        sum = sum + number

    print "The sum is", sum

main()
