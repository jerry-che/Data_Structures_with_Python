#  File: ExpressionTree.py

#  Description: demonstrates knowledge on binary trees 

#  Student's Name: Jerry Che

#  Student's UT EID: jc78222

#  Partner's Name: 

#  Partner's UT EID: 

#  Course Name: CS 313E

#  Unique Number: 86235

#  Date Created: 08/02/18

#  Date Last Modified: 08/06/18

operators=['+', '-', '*', '/']
pre = []
post = []

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

# Create Binary Node class with data and children
class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

# Create tree class with a root
class Tree (object):
  def __init__ (self):
    self.root = None

  # Follows algorithm given to make a tree from the given string expression
  def createTree (self, expr):
    s1 = Stack()

    expr = expr.split()
    current = Node(None)
    self.root = current

    for val in expr:
      if(val == '('):
        current.lchild = Node(None)
        s1.push(current)
        current = current.lchild
    
      elif(val in operators):
        current.data = val
        s1.push(current)
        current.rchild = Node(None)
        current = current.rchild

      elif(val==')'):
        if(s1.isEmpty() == False):
          current = s1.pop()
  

      else:
        current.data = val
        current = s1.pop()

  # Helper function to evaluate, performs rudamentary mathematics
  def operate (self, oper1, oper2, val):
    if (val == "+"):
      return oper1 + oper2

    elif (val == "-"):
      return oper1 - oper2

    elif (val == "*"):
      return oper1 * oper2

    elif (val == "/"):
      return oper1 / oper2

  # Runs evaluation of the binary tree
  def evaluate (self, aNode):
    s2 = Stack()

    expr = self.postOrder(self.root)

    for val in expr:
      if (val in operators):
        oper2 = s2.pop()
        oper1 = s2.pop()
        s2.push (self.operate (oper1, oper2, val))

      else:
        s2.push (float(val))

    return s2.pop()

  # pre order traversal - center, left, right - returns array
  def preOrder (self, aNode):
    if (aNode != None):
      pre.append(aNode.data)
      self.preOrder (aNode.lchild)
      self.preOrder (aNode.rchild)
    return pre

  # post order traversal - left, right, center - returns array
  def postOrder (self, aNode):
    if (aNode != None):
      self.postOrder (aNode.lchild)
      self.postOrder (aNode.rchild)
      post.append(aNode.data)
    return post

def main():

  expressiontree=Tree()

  expr_file = open ("expression.txt", "r")

  expr = expr_file.readline()

  expressiontree.createTree(str(expr))

  result = expressiontree.evaluate(expressiontree.root)

  print(str(expr), " = ", str(result))

  expressiontree.preOrder(expressiontree.root)
  print("Prefix Expression:", end=' ')

  for value in pre:
    print (value, end = " ")

  print("\n"+ "Postfix Expression:", end=' ')

  for value in post:
    print(value,end = " ")
main()