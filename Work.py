#  File: Work.py 

#  Description:  

#  Student Name: Jerry Che	

#  Student UT EID: jc78222 

#  Course Name: CS 313E

#  Unique Number: 86235

#  Date Created: 07/23/18

#  Date Last Modified:

def find_all_solutions(n,k):
	#Creates the variables
	total = n
	counter = 1

	#Sets the number of code lines 
	v = n // (k **counter) 

	#Validation lopp that exits right after the lines of code reaches 0
	while (v > 0):
		total +=v
		counter += 1
		v = n // (k**counter)

	#returns the total lines of code
	return total

def binarySearch (n, k):
  #Sets the variables of a binary search but instead sets hi to the number of code lines
  lo = 0
  hi = n

 #Sets a separate variable that will contain the minimum lines of code
  min_v = n

  # Whilw loop that mirrors binary search
  while (lo <= hi):
  	#Finds the middle
  	v = (lo + hi) // 2
  	#If it is bbigger than n move hi down
  	if (find_all_solutions(v,k) > n):
  		#If v is less than the current minimum, set the min_v to V
  		if v < min_v:
  			min_v = v
  		hi = v - 1 
  	#If it is smaller than move the lo up 1
  	elif find_all_solutions(v,k) < n:
  		lo = v + 1
  	#If it is right at the middle
  	else:
  		return v

  return min_v



def main():
	#Opens the file
	in_file = open("work.txt","r")

	#Takes the first element as the number of cases
	num_cases = int(in_file.readline())

	#Makes an empty list to add the number of lines to
	code_lines = []

	#goes through the file and converts the input into the data type inr
	for i in range (num_cases):
		line = in_file.readline().split()
		for j in range (len(line)):
			line[j] = int(line[j])
		code_lines.append(line)

	#Goes through the list and determines the correct value
	for case in code_lines:
		n,k = case[0],case[1]
		print(binarySearch(n,k))


	#Closes the file
	in_file.close()



main()