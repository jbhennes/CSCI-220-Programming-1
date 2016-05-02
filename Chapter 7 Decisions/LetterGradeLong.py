## LetterGradeLong.py

def main():
    
    print "Given a numerical grade, returns the letter grade."

    # Get the numerical grade
    grade = input("Enter your numerical grade: ")

    if grade >= 90:
        print "Letter grade = A"
    else:
        if grade >= 80:
            print "Letter grade = B"
        else:
            if grade >= 70:
                print "Letter grade = C"
            else:
                if grade >= 60:
                    print "Letter grade = D"
                else:
                    print "Letter grade = F"

main()
