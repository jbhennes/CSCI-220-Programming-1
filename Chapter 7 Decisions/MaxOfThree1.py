## MaxOfThree1.py
## Finds largest of three user-specified numbers 	

def main():
    
    x1 = input("Enter a number: ")
    x2 = input("Enter a number: ")
    x3 = input("Enter a number: ")

    # Determine which number is the largest

    if x1 >= x2 and x1 >= x3:     # x1 is largest	
        max = x1
    elif x2 >= x1 and x2 >= x3:   # x2 is largest
        max = x2
    else:                         # x3 is largest
        max = x3

    # display result	
    print "\nLargest number is", max

main()
