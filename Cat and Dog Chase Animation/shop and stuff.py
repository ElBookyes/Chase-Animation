TeslaColours = {"Red":15, "White":10, "Black":12, "Blue":9, "Grey":12}
print(TeslaColours)

while True:
    clientInput = input("Choose car colour: \n")
    if clientInput not in TeslaColours:
        print("Please select an available colour")
        continue
    if TeslaColours[clientInput] > 0:
        TeslaColours[clientInput] -= 1
    else:
        print("This colour of cars is out of stock \n Please select another colour")
    print(TeslaColours)

