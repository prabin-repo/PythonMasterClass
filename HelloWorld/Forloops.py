# name = "PRABIN KUMAR"

# for letters in name:
#     print(letters)

number="9.1112:222;333/-444,555"
separators=""

for ch in number:
    if not ch.isnumeric():
        separators=separators+ch

print(separators)
