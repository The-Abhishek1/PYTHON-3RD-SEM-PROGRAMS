# Create a list
my_list = ['apple', 'banana', 'cherry', 'orange']

# Append an item to the end of the list
my_list.append('pear')
print(my_list)

# Extend the list with another list
my_list.extend(['grape', 'kiwi'])
print(my_list)

# Insert an item at a specific index
my_list.insert(2, 'mango')
print(my_list)

# Remove and return the last item from the list
last_item = my_list.pop()
print(last_item)
print(my_list)

# Get a slice of the list
slice_of_list = my_list[1:4]
print(slice_of_list)

# Count the number of times an item appears in the list
count_of_item = my_list.count('banana')
print(count_of_item)
