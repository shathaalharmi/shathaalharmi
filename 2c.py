floor = input ("Enter the floor number: ")
floor = int(floor)
if floor > 13 :
    actualFloor = floor - 1
    print("The actual floor is ", actualFloor)
elif floor == 13:
    print("The floor 13 does not exist")
else :
    actualFloor = floor
    print("The actual floor is ", actualFloor)
    

price = float(input("enter the price : "))
if price >= 128 :
   discountedPrice = price * (1- 0.92)
else :
    discountedPrice = price * (1- 0.84)
print(" the price after discount i : ",discountedPrice)