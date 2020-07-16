available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "MousePad",
                   "Pendrive"]

Valid_Choice = []
for i in range(1, len(available_parts) + 1):
    Valid_Choice.append(str(i))
print(Valid_Choice)

current_choice = "_"
computer_parts = []

while current_choice != "0":
    if current_choice in Valid_Choice:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)

    else:
        print("PLease add from the below list")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()
print(computer_parts)
