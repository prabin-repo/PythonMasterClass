name=input("PLease enter your name :" )
Age=int(input("How old are you {0} ?".format(name)))
print(Age)

if Age < 18:
    print("{0} ! please come after {1} Years ".format(name, 18-Age))

elif Age == 150:
    print("{0} ! you are a dead man".format(name))

else:
    print("{0} ! you are eligible to vote".format(name, 18-Age))