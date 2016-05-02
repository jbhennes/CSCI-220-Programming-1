#inputErrorHandler.py

def main():
    print ("This program finds the real solutions to a quadratic")

    try:
        num = eval(input("Please enter an number: "))
        num = num + 1
        print ("Your number plus one equals " + str(num))
    except:
        print ("You must enter an number")
        
                  
    
