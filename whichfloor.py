maximum_stories = 21
work = input("On what floor of the the building is your office? ")
floor = int(work)

while (floor > maximum_stories):
    print(str(floor)+" is greater than the amount of floor in the building. These are 21 floors, please try again.")
    work = input("On what floor of the building is your office? ")
    floor = int(work)
print("Congratulations, floor "+str(floor)+" is your destination.")