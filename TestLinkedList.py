#  File: TestLinkedList.py

#  Description: a program demonstrating LinkedList

#  Student Name: Jerry Che

#  Student UT EID: jc78222

#  Partner Name: Terry Woodward Jr

#  Partner UT EID: tgw466

#  Course Name: CS 313E

#  Unique Number: 86235

#  Date Created: 07/28/18

#  Date Last Modified: 07/30/18

class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next


class LinkedList (object):
  def __init__ (self):
    self.first = None

  # get number of links 
  def getNumLinks (self):
  	counter = 0
  	current = self.first

  	if(current == None):
  		counter = 0
  	
  	while (current != None):
  		counter += 1
  		current = current.next

  	return counter
  
  # Add data at the beginning of the list
  def addFirst (self, data):
  	newLink = Link (data)
  	newLink.next = self.first
  	self.first = newLink

  # Add data at the end of a list
  def addLast (self, data):
  	newLink = Link(data)
  	current = self.first

  	if(current == None):
  		self.first = newLink
  		return

  	while(current.next != None):
  		current = current.next

  	current.next = newLink

  # Add data in an ordered list in ascending order
  def addInOrder (self, data):
  	newLink = Link(data)
  	current = self.first
  	previous = self.first

  	if(current == None):
  		self.first = newLink
  		return

  	while (current != None):
  		if(current.data <= data):
  			previous = current
  			current = current.next
  		else:
  			break

  	if(self.first.data >= data):
  		newLink.next = self.first
  		self.first = newLink
  	elif (current == None):
  		previous.next = newLink
  	else:
  		previous.next = newLink
  		newLink.next = current


  # Search in an unordered list, return None if not found
  def findUnordered (self, data):
  	current = self.first

  	if (current == None):
  		return None

  	while(current.data != data):
  		if(current.next == None):
  			return None
  		else:
  			current = current.next

  	return current

  # Search in an ordered list, return None if not found
  def findOrdered (self, data):
  	current = self.first

  	if(current ==  None):
  		return None

  	while (current.data != None and current.data < data):
  		if(current.next == None):
  			return None
  		else:
  			current = current.next

  	return current

  # Delete and return Link from an unordered list or None if not found
  def delete (self, data):
  	current = self.first
  	previous = self.first

  	if (current == None):
  		return None

  	while (current.data != data):
  		if (current.next == None):
  			return None
  		else:
  			previous = current
  			current = current.next

  	if (current == self.first):
  		self.first = self.first.next 
  	else:
  		previous.next = current.next

  	return current


  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
  	current = self.first
  	s = ""
  	count = 0

  	if (current == None):
  		return s

  	while (current != None):
  		s += str(current.data) + "  "
  		current = current.next
  		count += 1

  		if(count % 10 == 0):
  			s += "\n"
  			count = 0

  	return s

  # Copy the contents of a list and return new list
  def copyList (self):
  	current = self.first
  	copyList = LinkedList()

  	while (current != None):
  		copyList.addLast(current.data)
  		current = current.next

  	return copyList

  # Reverse the contents of a list and return new list
  def reverseList (self): 

  	current = self.first
  	copyList = LinkedList()

  	while (current != None):
  		copyList.addFirst(current.data)
  		current = current.next

  	return copyList


  # Sort the contents of a list in ascending order and return new list
  def sortList (self):
  	newList = LinkedList()
  	current = self.first

  	while(current != None):
  		newList.addInOrder(current.data)
  		current = current.next
  	return newList


  # Return True if a list is sorted in ascending order or False otherwise
  def isSorted (self):
  	current = self.first
  	previous = self.first

  	if current == None:
  		return True

  	while (current != None):
  		if current.data < previous.data:
  			return False
  		previous = current
  		current = current.next

  	return True

  # Return True if a list is empty or False otherwise
  def isEmpty (self): 
  	return self.first == None

  # Merge two sorted lists and return new list in ascending order
  def mergeList (self, b):
  	newList = LinkedList()

  	currentA = self.first
  	currentB = b.first

  	while(currentA != None) and (currentB != None):
  		if currentA.data < currentB.data:
  			newList.addLast(currentA.data)
  			currentA = currentA.next
  		else:
  			newList.addLast(currentB.data)
  			currentB = currentB.next

  	while currentA != None:
  		newList.addLast(currentA.data)
  		currentA = currentA.next

  	while currentB != None:
  		newList.addLast(currentB.data)
  		currentB = currentB.next

  	return newList


  # Test if two lists are equal, item by item and return True
  def isEqual (self, b):

  	currentA = self.first
  	currentB = b.first

  	if (currentA == None and currentB == None):
  		return True

  	if (self.getNumLinks != b.getNumLinks):
  		return False

  	while (currentA != None) and (currentB != None):
  		if (currentA.data != currentB.data):
  			return False

  		currentA = currentA.next
  		currentB = currentB.next

  	return True

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def removeDuplicates (self):
  	data_list = []
  	newList = LinkedList()
  	current = self.first

  	while(current != None):
  		data_list.append(current.data)
  		current = current.next

  	data_list = set(data_list)

  	for data in data_list:
  		newList.addLast(data)

  	return newList



def main():
  # Test methods addFirst() and __str__() by adding more than
  # 10 items to a list and printing it
  testList = LinkedList ()
  testList1 = LinkedList ()
  testList3 = LinkedList ()

  for i in range (11):
  	testList.addFirst(i)

  print(testList)

  # Test method addLast()
  for i in range (11):
  	testList1.addLast(i)
  print (testList1)

  # Test method addInOrder()
  list1 = [45,66,22,10,71,30,89,10]

  for item in list1:
  	testList3.addInOrder(item)
  print(testList3)


  # Test method getNumLinks()
  print(testList.getNumLinks())

  # Test method findUnordered() 
  # Consider two cases - item is there, item is not there 
  print(testList1.findUnordered(5))
  print(testList1.findUnordered(46))

  # Test method findOrdered() 
  # Consider two cases - item is there, item is not there 
  print(testList.findOrdered(5))
  print(testList.findOrdered(46))

  # Test method delete()
  # Consider two cases - item is there, item is not there
  testList.delete(5)
  print(testList) 

  print(testList.delete(46))


  #Test method copyList()
  print(testList1.copyList())

  # Test method reverseList()
  print(testList1.reverseList())

  # Test method sortList()
  testList4 = LinkedList()
  list2 = [10,3,45,89,33,66]

  for item in list2:
  	testList4.addLast(item)
  print(testList4.sortList())

  # Test method isSorted()
  # Consider two cases - list is sorted, list is not sorted
  print(testList4.isSorted())

  testList4 = testList4.sortList()

  print(testList4.isSorted())

  # Test method isEmpty()
  print(testList4.isEmpty())

  # Test method mergeList()
  print(testList4.mergeList(testList1))

  # Test method isEqual()
  # Consider two cases - lists are equal, lists are not equal
  testList5 = LinkedList()
  testList5 = testList1

  print(testList1.isEqual(testList5))
  print(testList1.isEqual(testList3))


  # Test removeDuplicates()
  print(testList3.removeDuplicates())

if __name__ == "__main__":
  main()