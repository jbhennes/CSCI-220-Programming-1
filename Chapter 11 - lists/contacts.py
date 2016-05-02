class Contacts:

    def __init__(self):
        self.contactNames = []

    def addContact(self, name):
        self.contactNames.append(name)

    def __str__(self):
        output = "Contacts:\n"
        for name in self.contactNames:
            output = output + name + " "
        output = output + "\n"
        return output
