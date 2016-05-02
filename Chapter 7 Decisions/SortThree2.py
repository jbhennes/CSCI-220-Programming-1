## SortThree2.py
## Sorts three user-specified numbers 	

def main():
    
    n1, n2, n3 = input("Enter three numbers separated by commas: ")

    # Define the outputs

    sorted1 = n1
    sorted2 = n2
    sorted3 = n3

    # Put the smallest value in sorted1

    if sorted1 > sorted2:     # Make sorted1 <= sorted2	
        temp = sorted1
        sorted1 = sorted2
        sorted2 = temp
        
    if sorted1 > sorted3:     # Make sorted1 <= sorted3	
        temp = sorted1
        sorted1 = sorted3
        sorted3 = temp

    # Now the smallest value is in sorted1


    # Put the next smallest value in sorted2

    if sorted2 > sorted3:     # Make sorted2 <= sorted3	
        temp = sorted2
        sorted2 = sorted3
        sorted3 = temp


    # Display the results	
    print "\nSorted order of", n1, ",", n2, ",", n3,
    print "is", sorted1, ",", sorted2, ",", sorted3

main()
