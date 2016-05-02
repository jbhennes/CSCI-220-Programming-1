from contacts import Contacts

def main():
    myContacts = Contacts()
    print "My " + str(myContacts)

    myContacts.addContact("Mickey")
    myContacts.addContact("Fred")
    myContacts.addContact("Edward")
    myContacts.addContact("Harry")

    print "My " + str(myContacts)

    yourContacts = Contacts()
    yourContacts.addContact("Pat")

    print "Your " + str(yourContacts)
    print "My " + str(myContacts)

main()
