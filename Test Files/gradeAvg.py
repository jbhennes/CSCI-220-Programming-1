def gradeAverages(filename):
    infile = open((filename), "r")
    for line in infile:
        averageGrade = 0
        splitLine = line.split()
        grades = splitLine[1:]
        averageGrade = (sum(eval(grades)))/(len(grades))
        print((splitLine[0]) + ": ", (averageGrade))

def main():
    gradeAverages("grades.txt")
