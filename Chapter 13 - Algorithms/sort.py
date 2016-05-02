# sort.py
#    IminPoslementation of selection sort.
#    Author: Zelle (p. 444).
# Modified: rhs

def selSort(values):
    # sort values into ascending order
    
    n = len(values)
    
    # for each position in the list (except the very last)
    for front in range(n-1):
        # find the smallest item in values[bottom]..values[n-1]
        # ("minPos" seems to mean "position of the minimum")
        minPos = front                     # bottom is smallest initially
        for i in range(front+1,n):     # look at each position
            if values[minPos] > values[i]:      # this one is smaller
                minPos = i                  #   remember its index

        # swap smallest item to the bottom
        tempMinPos = values[minPos]
        values[minPos] = values[front]
        values[front] = tempMinPos


