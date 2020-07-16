import random

highest = 10

number = random.randint(1, highest)

print("please guess a number between 1 and  {}: ".format(highest))
guess = 0

while guess != number:
    guess = int(input())

    if guess == 0:
        print("you have exited!")
        break
    if guess == number:
        print("Well done you guessed at the first time")
        break
    else:
        if guess < number:
            print(" please think higher")
        else:
            print("please think lower")
            guess = int(input("please try again"))

            if guess == number:
                print("u got the correct")
            else:
                print("Sorry you are wrong")



