# gradeAssessment.py

from string import *

def main():
    avg = input("Enter your average: ")

    if avg >= 60.0:
        msg = "Passing"
        if avg < 70.0:
            msg = msg + " but marginal."
        else:
            msg = msg + "."
    else:
        msg = "Failing."
    print msg

main()
