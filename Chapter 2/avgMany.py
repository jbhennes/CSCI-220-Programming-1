# avgMany.py
#   A simple program to average several exam scores.  
#   Illustrates use of multiple input.

def main():
    print "This program computes the average of several exam scores."
    print

    scoreCount = input("Enter the number of scores: ")
    total = 0.0
    for count in range(scoreCount):
        score = input("Enter a score: ")
        total = total + score
    average = total / scoreCount

    print "The average of the scores is:", average

main()
