#  File: Josephus.py

#  Description: Solution to the Josephus problem

#  Student Name: Jerry Che

#  Student UT EID: jc78222

#  Partner Name: Terry Woodward Jr

#  Partner UT EID: tgw466

#  Course Name: CS 313E

#  Unique Number: 86235

#  Date Created: 07/30/18

#  Date Last Modified:08/02/18

class Link(object):
	def __init__(self,data,next = None):
		self.data = data
		self.next = next 


class CircularList(object):
  # Constructor
  def __init__ ( self ): 
  	self.first = None

  # Insert an element (value) in the list
  def insert ( self, item ):
  	newLink = Link(item)
  	current = self.first

  	if current== None:
  		self.first = newLink
  		self.first.next = self.first
  		return

  	while current.next != self.first:
  		current = current.next

  	current.next = newLink
  	newLink.next = self.first

  # Find the link with the given key (value)
  def find ( self, key ):
  	current = self.first
  	flag = self.first

  	if current == None:
  		return None

  	while (current.data != key):
  		if (current.next.data == flag.data):
  			return None
  		else:
  			current = current.next

  	return current

  # Delete a link with a given key (value)
  def delete ( self, key ):
  	current = self.first
  	previous = self.first 
  	flag = self.first

  	if current == None:
  		return None

  	while (current.data != key):
  		if(current.next.data == flag.data):
  			return None
  		else:
  			previous = current
  			current = current.next

  	if (current == self.first):
  		self.first = self.first.next
  	else:
  		previous.next = current.next
  		
  	currentA = self.first

  	while(currentA.next.data != flag.data):
  		currentA = currentA.next
  	currentA.next = self.first


  	return current


  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ):
  	if (self.first == None):
  		return None

  	current = self.find(start)

  	for j in range (1,n):
  		current = current.next

  	self.delete(current.data)
  	print(current.data)
  	return current.next

  # Return a string representation of a Circular List
  def __str__ ( self ):
  	string = ""
  	current = self.first

  	while(current.next != self.first):
  		string += str(current.data) + " "
  		current = current.next
  	string += str(current.data)

  	return string

def main():

	in_file = open("josephus.txt","r")

	num_soldiers = int(in_file.readline().strip())
	start = int(in_file.readline().strip())
	n = int(in_file.readline().strip())

	in_file.close()

	circle_list = CircularList()

	for i in range (1, num_soldiers + 1):
		circle_list.insert(i)

	for i in range (num_soldiers):
		start = circle_list.delete_after(start,n)
		start = start.data

	




	


main()


