## pi.py
##
## Approximates pi by adding terms of the series
## 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...
## 

import math

number = input("How many terms do you want to sum? ")

numerator = 4.0
denominator = 1.0
sum = 0.0
signSwitcher = 1.0

for count in range(number):
    term = (numerator / denominator) * signSwitcher
    #print term
    sum = sum + term
    denominator = denominator + 2.0
    signSwitcher = signSwitcher * -1.0
    
print "Approximation of pi = ", sum

difference = math.pi - sum

print "Difference from actual pi =", difference
