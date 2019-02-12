distance = 0
energy = 10

while distance >= 0:
    print("Would you like to walk or run?")
    travel_method = input()
    if energy <= 0:
        energy += 1
        print("used up a lot of energy lets walk, eat or go home")
    elif travel_method == "walk":
        distance += 1
        energy += 5
        print("distance from home is {}km".format(distance))
        print("energy level is {}".format(energy))
    elif travel_method == "run":
        distance += 5
        energy -= 5
        print("distance from home is {}km".format(distance))
        print("energy level is {}".format(energy))
    elif travel_method == "eat":
        energy +=10
        print("so delicious your energy level is now {}".format(energy))
    elif travel_method == "go home":
        print("well get out of here")
        break
    else:
        print("wrong input")
