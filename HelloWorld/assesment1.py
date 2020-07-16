parrot="Norwegian Blue"
print(parrot)
print(len(parrot))
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()
print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print()
print(parrot[3 - len(parrot)])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

name="PRABIN KUMAR"
print(name)
print(len(name))
print(name[0:6])
print(name[0:5])
print(name[:6])
print(name[:6] + name[6:])
print(name[:])
print(name[7:12])
print(name[0:6:2])
print(name[0::2])

value="1,233.433:655;753,554"
separator=value[1::4]
print(separator)

letters="abcdefghijklmnopqrstuvwxyz"
backward=letters[25:0:-1]
print(backward)

print(letters[-1:0:-25])

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-26:-1])
print(letters[::-1])
