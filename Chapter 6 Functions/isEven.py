# isEven(num) returns true if num is even and false if not
# input: number
# output: boolean

def isEven(num):
    return num%2==0

def main():
    for i in range(10):
        message = str(i) + " is "
        if isEven(i):
            message = message + "even."
        else:
            message = message + "odd."
        print message
    
main()
    
