# average4.py
#    A program to average a set of numbers
#    Illustrates a sentinel loop using an empty string as the sentinel.

#    This program can average negative as well as non-neegative numbers.

def main():
    total = 0.0
    count = 0
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = eval(xStr)
        total = total + x
        count = count + 1
        xStr = input("Enter a number (<Enter> to quit) >> ")
    print ("\nThe average of the numbers is", sum / count)

main()
