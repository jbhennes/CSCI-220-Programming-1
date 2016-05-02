# solveSeries.py
#
# will output the series:
#       1 + 2/3 + 3/5 + 4/7 + 5/9 + 6/11 ... + (num + 1)/(i + num)

def solveSeries(n):
    total = 0
    for i in range(n):
        num = i + 1
        denom = i + num
        total += (num/denom)
    return total
