def main():
   try:
      num = eval(input("Enter number: "))
   except NameError:
      print ("You must enter a number!")
      print ("Default value for num set to 0")
      num = 0
   num = num + 1
   print (num)

main()
