## SortThree1.py
## Sorts three user-specified numbers 	

def main():
    
    n1, n2, n3 = input("Enter three numbers separated by commas: ")

    # Determine which of the six orderings is applicable

    if n1 <= n2 and n2 <= n3:     # n1 <= n2 <= n2	
        sorted1 = n1
        sorted2 = n2
        sorted3 = n3
    elif n1 <= n3 and n3 <= n2:   # n1 <= n3 <= n2	
        sorted1 = n1
        sorted2 = n3
        sorted3 = n2
    elif n2 <= n1 and n1 <= n3:   # n2 <= n1 <= n3	
        sorted1 = n2
        sorted2 = n1
        sorted3 = n3
    elif n2 <= n3 and n3 <= n1:   # n2 <= n3 <= n1	
        sorted1 = n2
        sorted2 = n3
        sorted3 = n1
    elif n3 <= n1 and n1 <= n2:   # n3 <= n1 <= n2	
        sorted1 = n3
        sorted2 = n1
        sorted3 = n2
    else:                         # n3 <= n2 <= n1	
        sorted1 = n3
        sorted2 = n2
        sorted3 = n1

    # display results	
    print "\nSorted order of", n1, ",", n2, ",", n3,
    print "is", sorted1, ",", sorted2, ",", sorted3

main()
