def main():
   print("Calculate number of pages in a group of books")

   totalPages = 0
   numBooks = eval(input("Number of books: "))
   for i in range(numBooks):
##      message = "Number of pages in book " + str(i+1) + ": "
      numPages = eval(input("Number of pages: "))
      totalPages = totalPages + numPages
   print ("Total : " + str(totalPages))
