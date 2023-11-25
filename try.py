# name = input('enter file :')
# handle = open(name)
# # print(handle)

# counts = dict()
# for line in handle :
#     words = line.split()
#     print(words)
#     for word in words :
#         counts[word] = counts.get(word,0) +1
#         print(counts[word])
#         print(counts.get(word,0))

items_list = {
    'School Bag' : 0,
    'Tiffin Box' : 0,
    'Water Bottle' : 0
}

for word in items_list :
        items_list[word] = items_list.get(word,0) +2
        # print(items_list[word])
        # print(items_list.get(word,0)+1)
print(items_list)

# print(items_list['School Bag'])
# print(items_list.get('School Bag',0))
