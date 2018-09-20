#-------------------------------------------------------------------------------
#  File: Graph.py

#  Description: graph traversal

#  Student Name: Jerry Che

#  Student UT EID: jc78222

# Partner's Name: Terry Woodward Jr.

# Partner's UT EID: tgw466

#  Course Name: CS 313E

#  Unique Number: 86325

#  Date Created: 8/12/2018

#  Date Last Modified: 8/13/2018
#-------------------------------------------------------------------------------

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # given a label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex ( self, label):
    if not self.has_vertex (label):
      self.Vertices.append (Vertex (label))

      # add a new column in the adjacency matrix for the new Vertex
      nVert = len (self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)

      # add a new row for the new Vertex in the adjacency matrix
      new_row = []
      for i in range (nVert):
        new_row.append (0)
      self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # do the depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack()

    # mark vertex v as visited and push it on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False


  # return the the index of a vertex with a given vertex_label
  # if there are more than one vertices return any of the indices
  # label is a string, and index is an integer
  # return -1 if label is not found in the graph
  def get_index (self, vertex_label):
    nVert = len(self.Vertices)
    for i in range(nVert):
      if (self.Vertices[i]).label == vertex_label:
        return i
    return -1

  # return edge weight of edge starting at from_vertex_label
  # and ending at to_vertex_label
  # from_vertex_label and to_vertex_label are strings
  # returns an integer
  # return -1 if edge does not exist
  def get_edge_weight (self, from_vertex_label, to_vertex_label):
    start = self.get_index(from_vertex_label)
    finish = self.get_index(to_vertex_label)
    weight = self.adjMat[start][finish]
    return weight

  # return a list of indices of immediate neighbors that
  # you can reach from the vertex with the given label
  # vertex_label is a string and the function returns a list of integers
  # return empty list if there are none or if the given label is not
  # in the graph
  def get_neighbors (self, vertex_label):
    neighbors = []
    start = self.get_index(vertex_label)
    nVert = len(self.Vertices)
    for i in range(nVert):
        if self.adjMat[start][i] > 0:
            neighbors.append(self.Vertices[i])
    return neighbors

  # return a list of the vertices in the graph
  # returns a list of Vertex objects
  def get_vertices (self):
    verts = []
    nVert = len(self.Vertices)
    for i in range(nVert):
        verts.append(self.Vertices[i].label)
    return verts

  # delete an edge from the graph
  # from_vertex_label and to_vertex_label are strings
  # if there is no edge, does nothing
  # does not return anything
  # make sure to modify the adjacency matrix appropriately
  def delete_edge (self, from_vertex_label, to_vertex_label):
    start = self.get_index(from_vertex_label)
    finish = self.get_index(to_vertex_label)
    self.adjMat[start][finish] = 0

  # delete a vertex from the graph
  # vertex_label is a string
  # if there is no such vertex, does nothing
  # does not return anything
  # make sure to remove vertex from vertex list AND
  # remove the appropriate row/column of the adjacency matrix
  def delete_vertex (self, vertex_label):
    vert = self.get_index(vertex_label)
    self.Vertices.remove(self.Vertices[vert])
    nVert = len(self.Vertices)
    for i in range(nVert):
      del self.adjMat[i][vert]
    del self.adjMat[vert]


def main():
  # create a Graph object
  cities = Graph()

  # open file for reading
  in_file = open("graph.txt", "r")

  # read the Vertices
  num_vertices = int ((in_file.readline()).strip())
  print (num_vertices)

  for i in range (num_vertices):
    city = (in_file.readline()).strip()
    print (city)
    cities.add_vertex (city)

  # read the edges
  num_edges = int((in_file.readline()).strip())
  print (num_edges)

  for i in range (num_edges):
    edge = (in_file.readline()).strip()
    print (edge)
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.add_directed_edge (start, finish, weight)

  # print the adjacency matrix
  print ("\nAdjacency Matrix")
  for i in range (num_vertices):
    for j in range (num_vertices):
        print(cities.adjMat[i][j],end = ' ')
    print ()
  print()

  # read the starting vertex for dfs and bfs
  start_vertex = (in_file.readline()).strip()
  print (start_vertex)

  # get the index of the starting vertex
  start_index = cities.get_index (start_vertex)
  print (start_index)

  # do depth first search
  print ("\nDepth First Search from " + start_vertex)
  cities.dfs (start_index)
  print()


  #get index of a label
  print (cities.get_index('Dallas'))

  #get the weight of an edge
  print (cities.get_edge_weight('Dallas', 'Houston'))

  #get neighbors of a vertex
  print (cities.get_neighbors('Houston'))

  #list of vertices of the graph
  print (cities.get_vertices())

  #delete an edge from the graph
  cities.delete_edge('Dallas', 'Houston')
  print (cities.get_edge_weight('Dallas', 'Houston'))

  #delete vertex from the graph
  cities.delete_vertex('Houston')
  print (cities.get_vertices())

  # close the file
  in_file.close()

if __name__ == '__main__':
    main()
