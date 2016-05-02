# sumArithmeticProgression.py

def main():
    print ("This program asks the user for an upper limit.")
    print ("Then it adds the arithmetic progression (1, 2, 3, ...)")
    print ("from 1 up to and including the limit.")
    print ()

    limit = eval(input("What is the upper limit of the sequence? "))
    total = 0

    for i in range(1, limit + 1):
        total = total + i

    print ("The sum of the arithmetic progression from 1 to", end =" ")
    print (limit,"is", total)

main()
