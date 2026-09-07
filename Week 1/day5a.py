fasting = "Autophagy Marathon"
cold_shower = True

# Write your if/elif/else logic below
if fasting == "Autophagy Marathon":
   print("48 hours active")
else:
   print("On a good track. Do better next time")
if cold_shower == True:
   print("Cold shower: Done")
else:
   print("No cold shower done. Get serious")
if fasting == "Autophagy Marathon" and cold_shower == True:
   print("Peak discipline day")
else:
   print("Tomorrow is another day, redo")
   # Ask the user for a number and print its multiplication table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")