Available_parts = ["Monitor",
                 "Keyboard",
                 "Mouse",
                 "Mouse Mat",
                 "Pendrive",
                 "HDMI cable"
                 ]

current_choice = "_"
computer_parts = []

while current_choice != '0':
    if current_choice in "123456":
        print("Adding parts {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("Monitor")
        elif current_choice=='2':
            computer_parts.append("Keyboard")
        elif current_choice == '3':
            computer_parts.append("Mouse")
        elif current_choice == '4':
            computer_parts.append("Mouse Mat")
        elif current_choice == '5':
            computer_parts.append("Pendrive ")
        elif current_choice == '6':
            computer_parts.append("HDMI cable")
    else:
        print("please add options from below list:")
        # for part in Available_parts:
        #     print("{0}: {1}".format(Available_parts.index(part)+1, part))
        for number, part in enumerate(Available_parts):
              print("{0}: {1}".format(number + 1 , part))
    current_choice = input()

print(computer_parts)