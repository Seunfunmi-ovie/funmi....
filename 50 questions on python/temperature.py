total = 0

for count in range(5):

   temperature = int(input("Enter temperature: "))
   convertion = temperature * 1.8 + 32
   total += convertion
   print(total)
