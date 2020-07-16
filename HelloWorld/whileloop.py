i = 0

while i < 10:
    print("i is now {}".format(i))
    i+= 1

print("-----------")

Available_exit=["north", "south", "east", "west"]
Chosen_exit=""

while Chosen_exit not in Available_exit:
    Chosen_exit=input("Enter the exit direction: ")
    if Chosen_exit.casefold() == "quit":
        print("Game Over")
        break
print("Perfect")