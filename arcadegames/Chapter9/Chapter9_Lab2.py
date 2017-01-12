import random

def create_list(list_size):
	""" Parameter: list size. returns: a list of random values 1-6
	list should be of length, list_size """
	newList = [""] * list_size
	for i in range(len(newList)):
		newList[i] = random.randint(1, 6)
	return newList

def count_list(list, number):
	""" Parameters: Takes in a list and a number
	Returns: the number of times the "number" appears in the list."""
	total = 0
	for i in range(len(list)):
		if number == list[i]:
			total += 1
	return total

def average_list(list):
	""" Parameters: list. Returns: average value of integers of list"""
	total = 0;
	i = 0;
	for i in range(len(list)):
		total += list[i]
	return total/(i+1) #because index 0



def main():
	my_list = create_list(10000)
	for i in range(1,7):
		count = count_list(my_list,i)
		print ("Count for value ", i, "is: ", count)
	avg = average_list(my_list)
	print(avg)



# Main 
main()