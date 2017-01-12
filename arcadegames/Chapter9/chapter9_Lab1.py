def min3(x, y, z):
	if (x < y) & (x < z):
		return x
	elif (y < x) & (y < z):
		return y
	else:
		return z

def print_min3():
    print(min3(4, 7, 5))
    print(min3(4, 5, 5))
    print(min3(4, 4, 4))
    print(min3(-2, -6, -100))
    print(min3("Z", "B", "A"))

def box(height, width):
    # Accepts parameters height, width. outputs box using *'s
    for column in range(height):
        for row in range(width):
            print ("*", end=" ")
        print()

def print_box():
    box(7,5)  # Print a box 7 high, 5 across
    print()   # Blank line
    box(3,2)  # Print a box 3 high, 2 across
    print()   # Blank line
    box(3,10) # Print a box 3 high, 10 across

def find(str, key):
    # Takes parameters my_list and key. Searches list for value contained in key.
    # Each time function finds key value, print the array position of key.
    for i in range(len(str)):
        if str[i] == key:
            print ("Found " , key , " at position " , i)



def print_find():
    my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17] 
    find(my_list, 12)
    find(my_list, 91)
    find(my_list, 80)

##### main
def main():
    #print_min3()
    #print_box()
    #print_find()


main()






