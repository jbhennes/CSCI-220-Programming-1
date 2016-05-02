from Date import Date

def main():
   d1 = Date()
   d1.setDate(4,13,2010)
   d2 = Date()
   d2.setDate(4,1,2009)
   d3 = Date()
   d3.setDate(1, 1, 2010)

   dates = []
   dates.append(d1)
   dates.append(d2)
   dates.append(d3)

   for date in dates:
      print (date)

   d2.setDate(5,1,2010)
   print(d2)
   print(dates[1])
   

main()
