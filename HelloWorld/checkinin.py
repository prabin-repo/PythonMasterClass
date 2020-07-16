String = "Prabin Kumar"
letter = input("Please input a letter or word !")

if letter in String:
    print("{} is in {}.".format(letter,String))
else:
    print("{} is not in {}".format(letter,String))