for i in range(1,5):
    for j in range(1,5):
        print("{0} times {1} is {2}".format(j, i, i * j))
    print("------")

print("*"*40)

for i in range(1,5):
    for j in range(i):
        print(i,end="")
    print()


