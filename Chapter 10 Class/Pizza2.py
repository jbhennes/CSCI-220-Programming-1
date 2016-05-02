# pizzaClass.py

class Pizza:

    def __init__(self, size):
        if size == 8 or size == 10 or size == 12:
            self.size = size
        else:
            self.size = 8
        self.toppings = []
        self.price = -1
        self.numSlices = -1

    def setPrice(self, price):
        if price >= 0:
            self.price = price
        else:
            self.price = -1

    def getPrice(self):
        return self.price

    def getNumSlices(self):
        return self.numSlices

    def cut(self):
        self.numSlices = int(self.size * 1.2)

    def buildPizza(self, toppings):
        for topping in toppings:
            self.toppings.append(topping)

    def serve(self, num):
        if self.numSlices >= num:
            self.numSlices -= num
        else:
            return 'Not enough Pizza'

    def __str__(self):
        rtnStr = 'Pizza:\n'
        rtnStr += '\tSize: ' + str(self.size) + ' inches\n'
        rtnStr += '\tToppings: '
        for topping in self.toppings:
            rtnStr += str(topping) + ' '
        rtnStr += '\n\tPrice: $ {0:.02f}'.format(self.price) + '\n'
        rtnStr += '\tNumber of Slices Left: ' + str(self.numSlices)
        return rtnStr
        
