# average1.py
#    text p. 234
#    A program to average a set of numbers.
#    Illustrates a counted loop (for loop) with an accumulator.

def main():
    n = eval(input("How many numbers do you have? "))
    sum = 0.0
    for i in range(n):
        x = eval(input("Enter a number >> "))
        sum = sum + x
    print ("\nThe average of the numbers is: ", (sum / n))

main()
