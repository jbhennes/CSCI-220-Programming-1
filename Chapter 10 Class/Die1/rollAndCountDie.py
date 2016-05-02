# rollAndCountDie.py

# Creates a single die object, then rolls it a prescribed number
# of times. Counts how many times each number comes up.

from die import Die

def main():
    theDie = Die()

    count = eval(input("How many times should I roll the die? "))

    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0

    for i in range(count):
        theDie.roll()
        val = theDie.getFaceValue()
        if val == 1:
            c1 = c1 + 1
        elif val == 2:
            c2 = c2 + 1
        elif val == 3:
            c3 = c3 + 1
        elif val == 4:
            c4 = c4 + 1
        elif val == 5:
            c5 = c5 + 1
        elif val == 6:
            c6 = c6 + 1
        else:
            print ("Error - value of die was", val)

    c1Percent = float(c1)/count * 100
    c2Percent = float(c2)/count * 100
    c3Percent = float(c3)/count * 100
    c4Percent = float(c4)/count * 100
    c5Percent = float(c5)/count * 100
    c6Percent = float(c6)/count * 100

    print ("Value 1 came up:", c1, "or a percentage of", c1Percent)
    print ("Value 2 came up:", c2, "or a percentage of", c2Percent)
    print ("Value 3 came up:", c3, "or a percentage of", c3Percent)
    print ("Value 4 came up:", c4, "or a percentage of", c4Percent)
    print ("Value 5 came up:", c5, "or a percentage of", c5Percent)
    print ("Value 6 came up:", c6, "or a percentage of", c6Percent)
        

main()
