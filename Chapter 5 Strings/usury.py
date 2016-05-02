# RoxAnn H. Stalvey
# Program 1 CSCI 220 Spring 2008 Solution
#
#    usury.py
#    Input: Principal, interest, number of months of loan
#    Output: The monthly payment for said loan, the total amount paid over
#            life of loan and the total interest paid


def main():
    #Statement of purpose
    print "This program acts as a loan calculator."

    #User input
    principal = input("Enter the loan amount: ")
    interest = input("Enter the interest rate (e.g.5.3%, enter 5.3): ")
    months = input("Enter the number of months for the loan: ")

    #Calculations
    rate = interest / 1200.
    ratePower = (1. + rate) ** months
    payment = (principal * rate * ratePower)/(ratePower - 1.)
    totalPaid = payment*months
    totalInterest = totalPaid - principal

    print "The monthly payment is $", payment
    print "The total amount paid over the life of the loan is $",totalPaid
    print "The total interest paid is $",totalInterest

main()  
    
    

    
