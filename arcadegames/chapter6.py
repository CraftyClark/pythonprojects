# for row in range(10):
#     for j in range(row):
#         print (" ",end=" ")
#     for j in range(10-row):
#     	print (j,end=" ")
 
#     # Print a blank line
#     # to move to the next row
#     print()


# for row in range(10):
# 	for column in range(10-row):
# 		print (column,end=" ")

# 	print()

# for row in range(1,10):
# 	for column in range(1,10):
# 		print (row*column,end=" ")
# 		if(row*column<10):
# 			print (" ",end="")


# 	print()

for i in range(10):
    # Print leading spaces
    for j in range(10-i):
        print (" ",end=" ")
    # Count up
    for j in range(1,i+1):
        print (j,end=" ")
    # Count down
    for j in range(i-1,0,-1):
        print (j,end=" ")
    # Next row
    print()




