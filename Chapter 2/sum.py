# sum.py

def main():
    print ("This program asks how many numbers the user will enter.")
    print ("Then it asks for the numbers and adds them up.")

    howMany = eval(input("How many numbers do you want to add? "))
    total = 0

    for count in range(howMany):
        number = eval(input("Enter a number: "))
        total = total + number

    print ("The sum is", total)

main()
