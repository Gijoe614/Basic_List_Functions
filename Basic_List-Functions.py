cars = []
newcars = ""

print ("Please enter types of cars, when finished enter done")
while newcars != "done":
    newcars = raw_input("Please enter a type of car: ")
    if newcars != "done":
        cars.append(newcars)

cars.sort()


print cars



