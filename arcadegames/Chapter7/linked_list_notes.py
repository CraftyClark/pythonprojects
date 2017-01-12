Similiar to array.
List can be resized, but array cannot. 
type( [2,3,4,5] ) = list 

It is easy to get the value given the location, 
but it is harder to get the location given the value.

---ITERATING (LOOPING) THROUGH A LIST---
2 ways to loop through a linked list
	1st)Using a for-each loop
		-Takes collection of items and loops once per items
		-It will take a copy of the item and store in a variable
		for processing.
			for item_variable in list_name:
	2nd)Using an index variable and directly access the list
		rather than through a copy for each item.
		-program counts from 0 up to the length of the list.
			for i in range(len(my_list)):

	*This 2nd method is more complex, but more powerful.
	Because we are working directly w/ the list elements,
	rather than just a copy, the list can be modified. 
		-The 1st method (for-each) does NOT allow 
		modification of the original list. 

Python does not implement a list as an array data type.

---ADDING TO A LIST---
To create a list from scratch, it is necessary to create a blank
list and then use the append function. Example below. 
	my_list = [] # Empty list
	for i in range(5):
	    user_input = input( "Enter an integer: ")
	    user_input = int(user_input)
	    my_list.append(user_input)
	    print(my_list)
	    
if a program needs to create an array of a specific length,
all with the same value, you could use this trick. 
	# Create an array w/ 100 zeros
	my_list = [0] * 100

---SUMMING OR MODIFYING A LIST---
Creating a running total of an array is a common operation.
Here is how it is done:
	# Summing the values in a list version 1
	my_list = [5,76,8,5,3,3,56,5,23]
	 
	# Initial sum should be zero
	list_total = 0
	 
	# Loop from 0 up to the number of elements
	# in the array:
	for i in range(len(my_list)):
	    # Add element 0, next 1, then 2, etc.
	    list_total += my_list[i]
	 
	# Print the result
	print(list_total)

The same thing can be done by using a for loop to iterate the array,
rather than count through a range:
	# Summing the values in a list version 2
	# Copy of the array to sum
	my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]
	 
	# Initial sum should be zero
	list_total = 0
	 
	# Loop through array, copying each item in the array into
	# the variable named item.
	for item in my_list:
	    # Add each item
	    list_total += item
	 
	# Print the result
	print(list_total)

Again note, that in order to actually change the original array.
The loop method, for i in range(len(my_list)): must be used. The loop 
method for item in my_list: cannot change the original array Because
'item' is just a copy, not the original element. 

---SLICING STRINGS---
Strings are actually list of characters. They can be treated like 
lists with each letter, being a seperate item. 

	x = "This is a sample string"
	#x = "0123456789"
	 
	print("x=", x)
	 
	# Accessing a single character
	print("x[0]=", x[0])
	print("x[1]=", x[1])
	 
	# Accessing from the right side
	print("x[-1]=", x[-1])
	 
	# Access 0-5
	print("x[:6]=", x[:6])
	# Access 6
	print("x[6:]=", x[6:])
	# Access 6-8
	print("x[6:9]=", x[6:9])

---UTF-8 CODE---

This next program takes a string and converts each value into
UTF-8 code, adds 1 to it, converts back to regular characters, 
and then prints it out. 
Then it converts back to UTF-8 again. Subtracts the 1 back from it. 
Converts back to original text again. And when you print it out,
you find the string it back to its original text.

plain_text = "This is a test. ABC abc"
 
encrypted_text = ""
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print(encrypted_text)
##prints: Uijt!jt!b!uftu/!BCD!bcd 

plain_text = ""
for c in encrypted_text:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    plain_text = plain_text + c2
print(plain_text)
##prints: This is a test. ABC abc

---ASSOCIATIVE ARRAYS---
Python is not limited to using numbers as an array index.
It is also possible to use an associative array. 
An associative array works like this:

# Create an empty associative array
# (Note the curly braces.)
x = {}
 
# Add some stuff to it
x["fred"] = 2
x["scooby"] = 8
x["wilma"] = 1
 
# Fetch and print an item
print(x["fred"])
##prints: 2



















