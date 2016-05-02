# whereToGo.py


def main():
    today = input("Enter what day this is [S, M, T, W, R, F, Y]: ")
    today = today.upper()

    if today == "S" or today == "Y":
        raining = input("Is it raining? [y/n]: ")
        raining = raining.lower()
        if raining == 'y':
            print ("Sleep late")
        else:
            print ("Go outside")
    else:
        print ("Go to work")

main()
