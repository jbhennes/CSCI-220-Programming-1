import time
## The functions:
def change1(param):
    param = param + 1
    print ("In change1, parameter = ", param)
    
def change2(param):
    print ("In change2, parameter originally =", param)
    param = [100, 200, 300]
    print ("In change2, parameter = ", param)

def change3(param):
    param[2] = 1000
    print ("In change3, parameter = ", param)

def change4(cir):
    time.sleep(.5)
    for color in ["blue", "yellow","green", "purple","magenta","black"]:
        time.sleep(.4)
        cir.setFill(color)

def copyList(param):
   newList = []
   for item in param:
      newList = newList + param
   print("In copy, param =", param)
   print("In copy, newList =", newList)
   newList[2] = 1000
   print("In copy after change, newList =", newList)
   print("In copy after change, param =", param)
