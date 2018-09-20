#  File: TestBinaryTree.py

#  Description: Binary Tree helper functions

#  Student Name: Jerry Che

#  Student UT EID: jc78222

#  Partner Name: Terry Woodward Jr.

#  Partner UT EID: tgw466

#  Course Name: CS 313E

#  Unique Number: 86235

#  Date Created: 08/06/18

#  Date Last Modified: 08/09/18

class Node (object):
	def __init__(self,data):
		self.data = data
		self.lChild = None
		self.rChild = None

class Tree (object):
	def __init__(self):
		self.root = None

	def is_similar(self,sNode,pNode):

		if sNode == None and pNode == None:
			return True

		else:


			if (sNode == None and pNode != None) or (sNode != None and pNode ==  None):
				return False

			elif ((sNode.lChild != None or sNode.rChild != None) and (not(pNode.rChild != None or pNode.lChild != None))):
				return False

			elif ((not(sNode.lChild != None or sNode.rChild != None)) and (pNode.rChild != None or pNode.lChild != None)):
				return False

			elif(sNode.data != pNode.data):
				return False
			else:
				return self.is_similar(sNode.lChild,pNode.lChild)
				return self.is_similar(sNode.rChild,pNode.rChild)

	def print_level(self,pNode,level):

		if level == 0:
			if self.root == None:
				return

			else:
				return self.root

		if level > 1:
			return self.print_level(pNode.lChild,level - 1), self.print_level(pNode.rChild,level -1)

		else:
			print(str(pNode.data))



	def get_height(self,root):

		if root == None:
			return 0
		else:
			return (1 + max(self.get_height(root.lChild),self.get_height(root.rChild)))

	def num_nodes(self,fNode):
		if fNode == None:
			return 0
		else:
			return 1 + self.num_nodes(fNode.lChild) + self.num_nodes(fNode.rChild)

	def search (self, key):
		current = self.root
		while ((current != None) and (current.data != key)):
			if (key < current.data):
				current = current.lChild
			else:
				current = current.rChild

		return current

	def insert (self, val):
		newNode = Node (val)

		if (self.root == None):
			self.root = newNode
		else:
			current = self.root
			parent = self.root

			while (current != None):
				parent = current
				if (val < current.data):
					current = current.lChild
				else:
					current = current.rChild

			if (val < parent.data):
				parent.lChild = newNode
			else:
				parent.rChild = newNode


def main():

	tree1= Tree()
	tree2 = Tree()
	tree3 = Tree()

	data1 = [5,2,10,45,68,79,11,18]
	data2 = [5,2,10,45,68,79,11,18]
	data3 = [6,3,4,99,34,10]

	for i in data1:
		tree1.insert(i)
	
	for j in data2:
		tree2.insert(j)

	for k in data3:
		tree3.insert(k)

	print("Does Tree1 == Tree2?", tree1.is_similar(tree1.root,tree2.root))
	print("Does Tree1 == Tree3", tree1.is_similar(tree1.root,tree3.root))
	print()

	tree1.print_level(tree1.root,2)
	tree2.print_level(tree2.root,1)
	print()

	print(tree1.get_height(tree1.root))
	print(tree3.get_height(tree3.root))

	print(tree1.num_nodes(tree1.root))
	print(tree3.num_nodes(tree3.root))

main()

