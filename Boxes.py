#  File: Boxes.py

#  Description:

#  Student Name: Jerry Che	

#  Student UT EID: jc78222

#  Partner Name: Terry Woodward Jr.

#  Partner UT EID: tgw466

#  Course Name: CS 313E

#  Unique Number: 86235

#  Date Created: 07/18/2018

#  Date Last Modified: 07/23/2018
def sub_sets (a, b, lo,out):
	if (lo == len(a)):
		if(is_valid(b)):
			out.append(b)
			return
	else:
		c = b[:]
		b.append(a[lo])
		sub_sets(a,b,lo + 1,out)
		sub_sets(a,c,lo + 1, out)

def is_valid(boxes):
	for i in range(len(boxes) - 1):
		if not compare(boxes[i],boxes[i+1]):
			return False
	return True

def compare(box1,box2):
	return ((box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2]))

def main():
	#Read the file
	in_file = open("boxes.txt",'r')
	#Read the number of boxes
	num_boxes = int(in_file.readline())
	#Create an empty list
	boxes = []
	out_list = []
	#Reads the files
	for i in range(num_boxes):
		line = in_file.readline().split()
		for j in range (len(line)):
			line[j] = int(line[j])
		line.sort()
		boxes.append(line)

	in_file.close()

	boxes.sort()
	sub_sets(boxes,[],0,out_list)

	print("Largest Subset of Nesting Boxes")

	for i in [y for y in out_list if (len(y) == (len(max(out_list,key = len))))]:
		for j in i:
			print(j)
		print()
















	






		
		





main()