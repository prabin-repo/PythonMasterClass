import random

highest = 10
number = random.randint(1, highest)

print("please enter a value between 1 and {} :".format(highest))
guess = int(input())

if guess == number:
    print("Hey you got at the first time !!")
else:
    if guess < number:
        print("please guess higher")
    else:
        print("please guess lower")

    guess = int(input("pls try again :"))
    if guess == number:
        print("Well Done")
    else:
        print("Sorry you are wrong")
