# modulo.py

def main():
    limit = input("Please enter upper limit of dividend: ")
    divisor = input("Please enter divisor: ")
    for dividend in range(limit+1):
        print "The remainder of", dividend, "divided by", divisor,
        print "=", dividend % divisor

main()

    
