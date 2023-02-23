# Strings are immutable
my_string = "Hello, World!"
print(my_string)

# Attempting to modify the string results in a TypeError
# my_string[0] = "J"  # uncomment this line to see the error

# Lists are mutable
my_list = [1, 2, 3, 4, 5]
print(my_list)

# We can modify the list by changing an item's value
my_list[0] = 0
print(my_list)

# We can also add items to the list or remove items from the list
my_list.append(6)
print(my_list)

my_list.pop()
print(my_list)

# Tuples are immutable
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Attempting to modify the tuple results in a TypeError
# my_tuple[0] = 0  # uncomment this line to see the error
