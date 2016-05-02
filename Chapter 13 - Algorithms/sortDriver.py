## sortDriver.py

from sort import *

def main():
##    list1 = [18,12,1,24,6,30,8,3,15,22]
    list1 = ["18","12","1","24","6","224","30","8","3","15","22"]
    print ("Unsorted list:")
    print (list1)

    selSort(list1)

    print ("\nSorted list:")
    print (list1)

    list2 = ["ban", "home", "ant", "app", "antelope", "apple", "cow", "doe", "zoo"]
    print ("\nUnsorted list:")
    print (list2)

    selSort(list2)

    print ("\nSorted list:")
    print (list2)

##    listOfLs = [l1, list2, range(0,1)]
##    print (listOfLs)
##    selSort(listOfLs)
##    print (listOfLs)

main()
