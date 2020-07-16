age=24
print("My Age is " +str(age) + " Years")

age = 25
print("My Age is {0} Years".format(age))

print("There are {0} days in  {1}, {2}, {3}, {4}, {5} "
      .format(30,"jan" ,"march","June","August","October"))

print("jan:{2}, Feb:{0}, Mar:{2}, April:{1}, May:{1}, June:{1}, July:{2}, August:{2}"
      .format(28,30,31))

print("""jan:{2}
Feb:{0}
Mar:{2}
April:{1}
May:{1}
June:{1}
July:{2}
August:{2}""".format(28,30,31))