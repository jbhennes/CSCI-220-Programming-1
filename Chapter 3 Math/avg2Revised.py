# avg2.py
#   A simple program to average two exam scores.  

def main():
    print "This program computes the average of two exam scores."
    print

    score1 = input("Enter the first score: ")
    score2 = input("Enter the second score: ")

    # The following line doesn't produce a fractional part:
    average = (score1 + score2) / 2

    # The following line always produces a fractional part
    # (even if not needed):
    #average = float(score1 + score2) / 2

    print "The average of the scores is:", average

main()
