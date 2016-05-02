## MaxOfThree3.py
## Finds largest of three user-specified numbers 	

def main():
    
    x1 = eval(input("Enter a number: "))
    x2 = eval(input("Enter a number: "))

    if x1 > x2:
        temp = x1
        x1 = x2
        x2 = temp
        print ("here")
        
    print ("The numbers in sorted order are: ")
    print (str(x1) + " " + str(x2))
    
##    x3 = eval(input("Enter a number: "))
##    
##    # Determine which number is the largest
##
##    max = x1          # Is x1 the largest?
##    if x2 > max:     	
##        max = x2      # Maybe x2 is the largest.
##    if x3 > max:     	
##        max = x3      # No, x3 is the largest.
##
##    # display result	
##    print ("\nLargest number is", max)

main()
