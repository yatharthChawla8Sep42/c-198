numOfCustomers = int(input("\nEnter No. of People in Queue: "))
print("\n", "_"*50)

for customer in range(0, numOfCustomers):
  total = 0
  customerName = input("\nEnter Name: ")
  while True:
    quantity = int(input("\nEnter the Quantity of Item: "))
    cost = int(input("Enter the Cost of Item: "))
    total=+quantity*cost

    repeat = input("\nDo you want to add more items? (Y/y/N/n): ")
    if (repeat == "n" or repeat == "N"):
      break
  print("\n", "_"*50)
  print("\nName: ", customerName)
  print("Total Cost: $", total)
  print("\n*****THANKS FOR SHOPPING WITH US*****")
  print("\n", "_"*50)