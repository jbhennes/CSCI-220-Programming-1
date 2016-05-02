# loop practice

def main():
    #loop to print even numbers
    print "Even Numbers:"
    for i in range(5):
        even = i * 2
        print even
    print
    
    # loop to print odd numbers
    print "Odd Numbers:"
    for i in range(5):
        odd = i*2 + 1
        print odd
    print

    #Convert fahrenheit (from lab)
    print "Convert Celsius temps to Fahrenheit:"
    for i in range(3):
        celsius = input("Enter Celsius temperature: ")
        fahrenheit = (9.0 / 5.0) * celsius + 32
        print celsius, "C = ", fahrenheit, "F"
    print

    #ConvertTable (from lab) (0..100)
    print "Celsius to Fahrenheit Conversion Table"
    print "--------------------------------------"
    for i in range(11):
        celsius = i * 10
        fahrenheit = (9.0 / 5.0) * celsius + 32
        print celsius, "C = ", fahrenheit, "F"
    print

    #ConvertTable with different range (-50..50 C)
    print "Celsius to Fahrenheit Conversion Table"
    print "--------------------------------------"
    for i in range(11):
        celsius = i * 10 - 50
        fahrenheit = (9.0 / 5.0) * celsius + 32
        print celsius, "C = ", fahrenheit, "F"
    print

main()
