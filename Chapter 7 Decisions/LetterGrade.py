## LetterGrade.py

def main():
    
    print ("Given a numerical grade, returns the letter grade.")

    # Get the numerical grade
    grade = input("Enter your numerical grade: ")

    if grade >= 90:
        print ("Letter grade = A")
    elif grade < 90 and grade >= 80:
        print ("Letter grade = B")
    elif grade < 80 and grade >= 70:
        print ("Letter grade = C")
    elif grade < 70 and grade >= 60:
        print ("Letter grade = D")
    else:
        print ("Letter grade = F")

main()
