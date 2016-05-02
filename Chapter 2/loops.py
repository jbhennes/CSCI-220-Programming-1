# loops.py

def main():

    print ("#1")
    for i in range(5):
        print (i)


    print ("\n#2")
    for i in [1, 2, 3, 4, 5]:
        print (i, end = " ")

    print ("\n#3")
    for i in range(1):
        print (i, end = " ")

    print ("\n#4")
    for i in range(0):
        print (i)

    print ("\n#5")
    for i in range(-1):
        print (i)

    print ("\n#6")
    num = eval(input("Enter number of times to execute: "))
    for i in range(num):
        print (i)

main()

