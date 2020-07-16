Shopping_list = ["Shoes", "Cap", "Clothes", "Belt", "Sunglasses", "Deo",]

Item_to_Search = "Perfume"
Found_At = None

# for index in range(len(Shopping_list)):
#     if Shopping_list[index] == Item_to_Search:
#         Found_At = index
#         break

if Item_to_Search in Shopping_list:
    Found_At = Shopping_list.index(Item_to_Search)
# print("{} found at position {}".format(Item_to_Search,Found_At))

if Found_At is not None:
    print("{} found at position {}".format(Item_to_Search,Found_At))
else:
    print("{} not found".format(Item_to_Search))