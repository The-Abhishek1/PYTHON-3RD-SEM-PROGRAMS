# Define a string
my_string = "Hello, world!"

# Split the string into a list of words
my_list = my_string.split()
print(my_list) # Output: ['Hello,', 'world!']

# Search for a substring within the string
if "Hello" in my_string:
  print("Found the substring 'Hello'")
else:
  print("Did not find the substring 'Hello'")

# Modify the string by replacing a substring
new_string = my_string.replace("world", "universe")
print(new_string) # Output: "Hello, universe!"

# Join a list of strings into a single string
my_list = ["Hello,", "world!"]
new_string = " ".join(my_list)
print(new_string) # Output: "Hello, world!"

# Convert the string to upper case
new_string = my_string.upper()
print(new_string) # Output: "HELLO, WORLD!"

# Convert the string to lower case
new_string = my_string.lower()
print(new_string) # Output: "hello, world!"

#Search for a letter in string
print(my_string.find("Hello"))
