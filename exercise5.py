distance = 0

while distance >= 0:
    print("Would you like to walk or run?")
    travel_method = input()
    if travel_method == "walk":
        distance += 1
        print("distance from home is {}km".format(distance))
    elif travel_method == "run":
        distance +=5
        print("distance from home is {}km".format(distance))
    elif travel_method == "go home":
        print("well get out of here")
    else:
        print("wrong input")
