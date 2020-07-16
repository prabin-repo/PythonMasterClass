numbers = [10,20,30,41,50,60]

for values in numbers:
    print(values)
    if values % 8 == 0:
        print("Values are not acceptable")
        break
else:
    print("Values considered")
