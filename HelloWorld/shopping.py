shopping_list=["shoes","clothes","groceries","gifts","drinks"]

for items in shopping_list:
    print("Buy items " +items)
print("------------")
for items in shopping_list:
    if items !="drinks":
        print("Buy items " +items)

print("------------")

for items in shopping_list:
    if items=="drinks":
        continue
    print("Buy {} ".format(items))
print("------------")

for items in shopping_list:
    if items=="clothes":
        break
    print("Buy {} ".format(items))
print("------------")

shopping_list=["shoes","clothes","groceries","gifts","drinks"]
Item_To_Search  ="gifts"
Found_At = None

for indexAt in range(len(shopping_list)):
    if shopping_list[indexAt] == Item_To_Search:
        Found_At = indexAt
        break
print("Item found at position {}".format(Found_At))


