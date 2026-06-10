number = 25
while True:

   answer = int(input("Enter a number: "))

   if answer == number:
      print("Correct")
      break
   elif answer >= number:
      print("Too high")
   else:
      print("Too low")      
