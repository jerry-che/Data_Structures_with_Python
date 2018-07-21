#  File: BabyNames.py 

#  Description:  

#  Student Name: Jerry Che

#  Student UT EID: jc78222

#  Course Name: CS 313E

#  Unique Number: 86325

#  Date Created: 07/03/18

#  Date Last Modified: 07/06/18

import operator

def main():
	#Try and exception loops
	try:
		#Calls the method make a dictionary
		baby_dictionary = make_dict()

		#Asks the user for input
		user_choice = print_menu()

		#Depending on what the user chooses it will call the specific function
		if user_choice == 1:
			find_name(baby_dictionary)
		elif user_choice == 2:
			print_name(baby_dictionary)
		elif user_choice ==3:
			print_one_decade(baby_dictionary)
		elif user_choice == 4:
			all_decades(baby_dictionary)
		elif user_choice == 5:
			increasing_pop(baby_dictionary)
		elif user_choice ==6:
			decreasing_pop(baby_dictionary)
		else:
			quit()

	#Prints out and error if one is found in the try block
	except Exception as err:
		print (err)



#Creates a dictionary of baby names
def make_dict():
	#Opens a file and creats dictionary
	baby_file = open('names.txt','r')
	baby_dict = {}

	#Loops through and adds the key and values to the dictionry
	baby = baby_file.readline().rstrip().split()
	while len(baby) != 0:
		key = baby[0]
		values =[]
		for i in range (1,len(baby)):
			values.append(int(baby[i]))
		baby_dict[key] = values

		baby = baby_file.readline().rstrip().split()
	return baby_dict

#Prints out the menu and returns the user's choice
def print_menu():
	print (''' Options:
Enter 1 to search for names
Enter 2 to display data for one names
Enter 3 to display all names that appear in only one decade.
Enter 4 to display all names that appear in all decades
Enter 5 to display all names that are more popular in every decade
Enter 6 to display all names that are less popular in every decade
Enter 7 to quit
''')
	choice = int(input("Enter Choice:"))
	return choice


#Finds the name if it is in the baby dictionary
def find_name(names):
	found = False
	search_name = input("Enter a name:")

	#Iterates and finds the name
	for key in names:
		if key == search_name:
			found = True
			break

	#Prints out the following message 
	if found:
		print (search_name,"is found")

	else:
		print(search_name,"is not found in any decade")

#Finds the name and prints out the raniing per name
def print_name(names):
	search_name = input("Enter a name:")

	for key in names:
		if key == search_name:
			name_values = names[key]
			print (search_name + ':' + ' {} {} {} {} {} {} {} {} {} {} {}'.format(*name_values))
			print ('1900: {}\n1910: {}\n1920: {}\n1930: {}\n1940: {}\n1950: {}'.format(*name_values[0:6]))
			print('1960: {}\n1970: {}\n1980: {}\n1990: {}\n2000: {}\n'.format(*name_values[6:]))
			break
	print ('Name not found')

# Prints out the rankings for one decade
def print_one_decade(names):
	#Intialize variables
	years = ['1900','1910','1920','1930','1940','1950','1960','1970','1980','1990','2000']
	position = 0
	new_dict = {}

	#Asks the user for input
	decade = input('Enter decade: ')

	#If it is not a correct year prompts the user again
	while decade not in years:
		decade = input('Enter decade: ')

	#Sets the position of the  index
	if decade == 2000:
		position = 10
	else:
		decade.split()
		position = int(decade[2])

	#Goes though the dictionary and adds to the new dictionary if it is in the top 1000
	for key in names:
		rankings = names[key]

		if rankings[position] != 0:
			new_dict[key] = rankings[position]

	#Prints out all the rankings
	for key,value in sorted(new_dict.items(), key = operator.itemgetter(1)):
		print(key,":",value)

#Prints out all the names that are ranked each year
def all_decades(names):
	count = 0
	list_of_names = []

	#Checks to see if any of the values are 0
	for key in names:
		values = names[key]
		if 0 in values:
			pass
		else:
			list_of_names.append(key)

	print(str(len(list_of_names)), "names appear in every decade. The names are:")

	for i in range (len(list_of_names)):
		print(list_of_names[i])

#Checks to see if the names are increasing in popularity
def increasing_pop(names):
	
	list_of_names =[]
	increasing = None

	#Iterates through the list and if there are no zeros finds the one that is increasing
	for key in names:
		values = names[key]
		if 0 not in values:
			#If the value to the left is smaller than it can't be increasing
			for i in range (len(values) - 1):
				if values[i] <= values[i+1]:
					increasing = False
					break
				increasing = True
			if increasing:
				list_of_names.append(key)
		

	#Prints out the names
	print(str(len(list_of_names)), "names are more popular every decade")
	for i in range(len(list_of_names)):
		print (list_of_names[i])


#Checks and returns which names are decreasing in popularity 
def decreasing_pop(names):
	list_of_names =[]
	decreaing = None

	for key in names:
		values = names[key]

		#Goes through the list and replaces 0's with 1001
		for i in range (len(values)):
			if values[i] == 0:
				values[i] = 1001

		#Checks to see if the values are increasing 
		for j in range(len(values) - 1):
			if values[j] >= values[j+1]:
				decreasing = False
				break
			decreasing = True

		if decreasing:
			list_of_names.append(key)

	#Prints out the names 
	print(str(len(list_of_names)), "names are more popular every decade")
	for i in range(len(list_of_names)):
		print (list_of_names[i])

#Prints out goodbye
def quit():
	print("Goodbye")

main()




