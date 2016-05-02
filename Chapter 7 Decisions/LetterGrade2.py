## LetterGrade.py

def main():
    
    print "Given a numerical grade, returns the letter grade."

    # Get the numerical grade
    grade = input("Enter your numerical grade: ")

    # Exhaustive cases - every possible value is considered
    # Exclusive cases - no overlapping cases
    if grade >= 90:
        print "Letter grade = A"
    elif grade < 90 and grade >= 80:
        print "Letter grade = B"
    elif grade < 80 and grade >= 70:
        print "Letter grade = C"
    elif grade < 70 and grade >= 60:
        print "Letter grade = D"
    elif grade < 60:
        print "Letter grade = F"
    print "Completed conditional 1\n"

    if grade >= 90:
        print "Letter grade = A"
    elif grade < 60:
        print "Letter grade = F"
    elif grade < 90 and grade >= 80:
        print "Letter grade = B"
    elif grade < 80 and grade >= 70:
        print "Letter grade = C"
    elif grade < 70 and grade >= 60:
        print "Letter grade = D"
    print "Completed conditional 2\n"
        
    # Exhaustive case - not exclusive therefore order matters
    if grade >= 90:
        print "Letter grade = A"
    elif grade >= 80:
        print "Letter grade = B"
    elif grade >= 70:
        print "Letter grade = C"
    elif grade >= 60:
        print "Letter grade = D"
    else:
        print "Letter grade = F"
    print "Completed conditional 3\n"

    # Exhaustive - but error because of bad order
    if grade < 60:
        print "Letter grade = F"
    elif grade >= 60:
        print "Letter grade = D"
    elif grade >= 70:
        print "Letter grade = C"
    elif grade >= 80:
        print "Letter grade = B"    
    else:
        print "Letter grade = A"
    print "Completed conditional 4\n"
        

main()
