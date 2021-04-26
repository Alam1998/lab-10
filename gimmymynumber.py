userstring = input("Gimme ma number that is greater than 100...")
usernum = int(userstring)
while usernum<100:
	print(str(usernum) + " is less than 100, Try again, I've got all day...")
	userstring = input(str(usernum) + " is less than 100, Try again, I've got all day...")
	usernum = int(userstring)
print(str(usernum) + " is greater than 100! Finally! Great job!")
