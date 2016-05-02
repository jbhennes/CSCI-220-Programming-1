from Date import *

def main():
   today = Date()
   print(today)
   today.setDate(4, 16, 2012)
   print(today)
   today.setDate(2,29,1997)
   print(today)
   print("Month = " + str(today.getMonth()))
   print("Day = " + str(today.getDay()))
   print("Year = " + str(today.getYear()))
   today.setDate(12, 8, 1200)
   print(today)
   today.setDate(13, 8, 2012)
   print(today)
main()
