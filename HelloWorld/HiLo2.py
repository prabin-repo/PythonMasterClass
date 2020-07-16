low = 1
high = 1000

print("please think of a value between {} and {} ".format(low, high))
input("please ENTER to start")
guesses =1

while low != high:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. what should i guess now? Enter h , l, or c to reach the correct guess!! ".format(guess)).casefold()

    if high_low == "h":
        low = guess +1
    elif high_low == "l":
        high = guess -1
    elif high_low == "c":
        print("you got it with {} guesses".format(guesses))
        break
    else:
        print("please enter h, l or c")

    guesses +=1

else:
    print("you thought of the number {}".format(low))
    print("you got it with {} guesses".format(guesses))

