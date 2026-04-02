quantity = 34444
total = 1.3555
print("The total is %10.2f and the quantity is %3d " %(total, quantity))


CANS_PER_PACK = 6
userInput = input("please enter the price for a six-pack: ")
packPrice = float(userInput)

userInput = input("please enter the volume fo each can (in ounces):")
canVolum = float(userInput)

packVolume = canVolum * CANS_PER_PACK

pricePerOunce = packPrice / packVolume

print("price per ounce: %8.2f" % pricePerOunce)


floor = int(input("floor: "))
if floor > 13 :
    actualFloor = floor - 1
else :
    actualFloor = floor
print("The elelvator will travel to the actual floor", actualFloor)