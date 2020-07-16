shopping_list = ["milk","chocolates","fruits","juice"]
print(shopping_list)

for items in shopping_list:
    print(items)

extra_list=shopping_list
print(id(shopping_list))
print(id(extra_list))

shopping_list += ["icecream"]
print(shopping_list)
print(id(shopping_list))

a=b=c=d=e=f=extra_list
print(a)
print(b)
b.append("cream")
print(c)
print(d)
print(b)
print(id(c))
