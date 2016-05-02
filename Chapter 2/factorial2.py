#calculates factorial

def main():
   print ("Calculates factorial.\n")

   n = eval(input("Enter upper limit: "))

   total = 1
   for i in range(n, 0, -1):
     # print ("inside loop value to multiply is",i)
      total = total * i

   print(n,"! =", total)

main()
