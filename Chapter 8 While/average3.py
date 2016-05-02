# average3.py
#    text p. 240
#    A program to average a set of numbers.
#    Illustrates a sentinel loop using negative input as the sentinel.

#    This program can average only non-negative numbers.

def main():
    total = 0
    count = 0
    x = eval(input("Enter a number (negative to quit) >> "))
    while x >= 0:
        total = total + x
        count = count + 1
        x = input("Enter a number (negative to quit) >> ")
    print ("\nThe average of the numbers is", sum / count)

main()
