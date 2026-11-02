
list1 = [1, 2, 3, 4, 5]
list2 = [11, 12, 13, 14, 15]

list_zip = []
list_odd = []
list_zip_reverse = []

# 1. Combine lists alternately
for i in range(len(list1)):
    list_zip.append(list1[i])
    list_zip.append(list2[i])

# 2. Find odd integers
for i in list1:
    if i % 2 != 0:
        list_odd.append(i)

for i in list2:
    if i % 2 != 0:
        list_odd.append(i)

# 3. Combine lists in reverse order
for i in range(len(list1) - 1, -1, -1):
    list_zip_reverse.append(list1[i])
    list_zip_reverse.append(list2[i])

print("List_Zip: ", list_zip)
print("List_Odd: ", list_odd)
print("List_Zip_Reverse: ", list_zip_reverse)
