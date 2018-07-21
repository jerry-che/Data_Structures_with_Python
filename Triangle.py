#  File: Triangle.py

#  Description: finds the largest path sum of a triangle

#  Student's Name: Jerry Che

#  Student's UT EID: jc78222

#  Partner's Name: Terry Woodward Jr.

#  Partner's UT EID: tgw466

#  Course Name: CS 313E 

#  Unique Number: 86325

#  Date Created: 07/12/18

#  Date Last Modified: 07/15/18


import time
# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):

  grid_lines = len(grid)
  num_solutions = 2 ** (grid_lines - 1)
  maximum = 0

  for row in range (num_solutions):
    temp = int(grid[0][0])
    idx = 0
    for col in range (grid_lines - 1):
      idx = idx + (row >> col & 1)
      temp += int(grid[col+1][idx])
    if temp > maximum:
      maximum = temp

  return maximum

# returns the greatest path sum using greedy approach
def greedy (grid):
  p = 0
  greatest_sum = grid[0][0]

  for x in range(1, len(grid)):
    if p < x and (grid[x][p+1] > grid[x][p]):
      p +=1
    greatest_sum += grid[x][p]

  return greatest_sum



# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid,row,col):
  num_of_rows = len(grid)

  if row >= num_of_rows:
    return 0
  else:
    path1 = rec_search(grid,row + 1,col)
    path2 = rec_search(grid,row + 1, col + 1)
    final = max(path1,path2) + int(grid[row][col])

  return final;

  

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):

  grid_lines = len(grid)

  for row in range(grid_lines - 2, -1, -1):
    for col in range(row + 1):
      grid[row][col] = int(grid[row][col]) + max(int(grid[row+1][col]), int(grid[row+1][col+1]))
  value = grid[0][0]
  triangle = grid

  return value, triangle

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  rows = []

  with open("triangle.txt","r") as in_file:
    n = int(in_file.readline())
    for line in in_file:
      row = line.rstrip().split()
      row = [int(i) for i in row]
      rows.append(row)

  return n, rows

def main ():
  # read triangular grid from file
  n,rows = read_file()

  ti = time.time()
  # output greates path from exhaustive search
  final_sum = exhaustive_search(rows)
  tf = time.time()
  del_t = tf - ti

  print("The greatest path sum through exhaustive search is", format(final_sum))
  # print time taken using exhaustive search
  print("The time taken for exhaustive search is",str(del_t * 1000),"seconds")

  ti = time.time()
  # output greates path from greedy approach
  final_sum = greedy(rows)
  tf = time.time()
  del_t = tf - ti
  # print time taken using greedy approach
  print()
  print("The greatest path sum through greedy search is", format(final_sum))
  print("The time taken for exhaustive search is",del_t,"seconds")

  ti = time.time()
  # output greates path from divide-and-conquer approach
  final_sum = rec_search(rows,0,0)
  tf = time.time()
  del_t = tf - ti

  # print time taken using divide-and-conquer approach
  print()
  print("The greatest path sum through recursive search is", format(final_sum))
  print("The time taken for exhaustive search is",format(del_t,'.13f'),"seconds")

  ti = time.time()
  # output greates path from dynamic programming 
  final_sum, grid = dynamic_prog(rows)
  tf = time.time()
  del_t = tf - ti
  # print time taken using dynamic programming
  print()
  print("The greatest path sum through dynamic programming is", format(final_sum))
  print("The time taken for exhaustive search is",del_t,"seconds")

if __name__ == "__main__":
  main()
