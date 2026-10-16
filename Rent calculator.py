#INPUTS TO BE PROVIDED BY THE USER

#TOTAL RENT AMOUNT
#TOTAL FOOD ORDER AMOUNT
#TOTAL NUMBER OF PEOPLE SHARING THE ROOM
#ELECTRICITY BILL AMOUNT
#WATER BILL AMOUNT

rent = int(input("Enter the total rent amount:"))
food = int(input("Enter the total food order amount: "))
electricity_bill =int(input("Enter the electricity bill amount: "))
water_bill = int(input("Enter the water bill amount: "))
members = int(input("Enter the total number of people sharing the room: "))

output = (rent + food + electricity_bill + water_bill) // members
print("The total amount each person has to pay is :" , output)