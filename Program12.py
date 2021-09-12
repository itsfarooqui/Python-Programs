#12. Write a method to remove duplicate elements from an array.

my_list = [1, 2, 3, 1, 2, 4, 5, 4 ,6, 2]
print("List Before ", my_list)
temp_list = []

for i in my_list:
    if i not in temp_list:
        temp_list.append(i)

my_list = temp_list

print("List After removing duplicates ", my_list)