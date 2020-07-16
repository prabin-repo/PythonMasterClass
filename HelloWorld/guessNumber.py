number=5
print("Enter a value between 1 to 10 : ")
guess=int(input())


if guess==number:
    print("you guessed it correct at first time")
else:
    if guess<number:
        print("guess higher")
    else:
        print("guess Lower")
    guess=int(input())
    if guess==number:
        print("you have guessed correct")
    else:
        print("Sorry you are wrong")



# if guess<number:
#     print("Please think a higher")
#
# elif guess>number:
#     print("please think a bit lower")
#
# else:
#     print("you have guessed the correct number !!")