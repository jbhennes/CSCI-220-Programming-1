# Mileage1 - Does my car get good mileage?

def main():    

    for i in range(2):
        mpg = eval(input("Enter the miles per gallon you get: "))
        print()
        cond = mpg < 20 and mpg > 10
        if mpg < 20.0 and mpg > 10:
            print("You need a more efficient car!")
        elif mpg >= 35:
            print("Thanks for helping the environment!")
        elif mpg > 25 and mpg < 30:
            print("Print bettter than 25")
        print()   
    print("\nDone")

main()
