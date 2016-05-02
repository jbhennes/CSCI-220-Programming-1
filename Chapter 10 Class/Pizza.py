# Stalvey
# Inclass exercise
# Class development

class Pizza:
    #sets values for attributes: size, numSlices, toppings, and price
    #accepts size from calling program.  Allowed sizes are 8, 10, or 12
    def __init__(self, size):
        if size == 8 or size == 10 or size == 12:
            self.size = size
        else:
            self.size = 8
        self.price = -1
        self.toppings = []
        self.numSlices = -1

    #setter
    #price must be greater than or equal to 0
    def setPrice(self, price):
        if price >= 0:
            self.price = price

    #getters
    def getPrice(self):
        return self.price

    def getNumSlices(self):
        return self.numSlices

    #cut() divides the pizza based on its size
    def cut(self):
        self.numSlices = int(self.size * 1.2)

    #buildPizza() accepts a list of toppings and clones this list
    #for self.toppings 
    def buildPizza(self, toppings):
##        self.toppings = toppings #alias - maybe a bad idea
        #To avoid, create a clone...
        for topping in toppings:
            self.toppings.append(topping)

    #method to remove num from numSlices as long as num is not too large
    def serve(self,num):
        if self.numSlices >= num:
            self.numSlices = self.numSlices - num

    def __str__(self):
        output = str(self.size) + "\" pizza"
        output = output + "\nIngredients: "
        for topping in self.toppings:
            output = output + str(topping) + " "
        output = output + "\nNumber of slices: " + str(self.numSlices)
        output = output + "\nPrice: $ {0:.02f}".format(self.price)
        return output

        

        
