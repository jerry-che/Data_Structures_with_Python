'''
  File: MagicSquare.py

  Description: Creates a magic square and checks to see if it is a magic_square

  Student's Name: Jerry Che

  Student's UT EID: jc78222

  Partner's Name: Terry Woodward Jr

  Partner's UT EID: tgw466

  Course Name: CS 313E 

  Unique Number: 86325

  Date Created: 06/15/2018

  Date Last Modified: 
'''

def main():

  #Prompts the user to enter an odd number 1 or greater 
  user_input = int(input("Please enter an odd number:"))

  #Checks to see if it is odd, positive, and greater than or equal to 3
  while (user_input % 2 == 0) or (user_input < 0):
    user_input = int(input("Please enter an odd number:"))

  #Calls the functions
  magic_square = make_square(user_input)
  print_square(magic_square)
  print()
  check_square(magic_square)



def make_square(n):
    #Creates an empty 2D list and fills it with None
    square_list =[[None for x in range(n)] for y in range (n)]

    #Sets the position of 1 and the number
    num = 1
    i = n-1
    j = n//2

    #Validation loop to fill the square
    while num <= (n*n):
      #Checks to see if it falls out of bottom bound
      if i == n :
        i = 0
      #Checks to see if it falls out of right bound
      if j == n:
        j = 0
      #Checks to see if it is in the right corner
      if (i== n) and (j == n):
        i = i -2
        j = j -1

      #Checks to see if the square is filled
      if(square_list[i][j] != None):
        i = i - 2
        j = j - 1
        continue

      # Fills the square up
      else:
        square_list[i][j] = num
        num+=1

      #changes the postion by moving it right and down
      i+=1
      j+=1 

    return square_list



def print_square(magic_square):
  print()
  # Prints out a introductory statement
  print("Here is a", str(len(magic_square)), 'x',str(len(magic_square)),'magic square:')

  # Nested loop to print out the square
  for i in range (len(magic_square)):
    for j in range(len(magic_square[i])):
      print (str(magic_square[i][j]).rjust(2),end ="   ")
    print()

  



def check_square(magic_square):

  #Creates all the method values for this class
  is_magic_square = True
  n = len(magic_square)
  canonical_sum = int((n *((n**2)+1)) / 2)

# Checks the column sum
  for x in range (len(magic_square)):
    column_sum = 0
    for y in range(len(magic_square[x])):
      column_sum += magic_square[y][x]

    #If one of the columns doesn't equal the canonical sum then it returns false
    if (column_sum != canonical_sum):
      is_magic_square = False

  #Checks the row sum
  for x in range (len(magic_square)):
    row_sum = 0
    for y in range(len(magic_square[x])):
      row_sum += magic_square[x][y]

    #If one of the rows doesn't equal the canonical sum then it returns false
    if(row_sum != canonical_sum):
      is_magic_square = False

  #Checks the LR sum
  lr_sum = 0
  for x in range(len(magic_square)):
    lr_sum += magic_square[x][x]

  #If the diagonal doesn't equal the canonical sum then it returns false
  if (lr_sum != canonical_sum):
    is_magic_square = False

  #Checks the RL Sum
  rl_sum = 0
  for x in range(len(magic_square)):
    rl_sum += magic_square[x][(len(magic_square)-1) - x]

  #If the diagonal doesn't equal the canonical sum then it returns false
  if (rl_sum != canonical_sum):
    is_magic_square = False

  #Prints out the correct statement based on if it is a magic square
  if (is_magic_square == True):
    print("This is a magic square and the canonical sum is", str(canonical_sum))
  else:
    print("This is not a magic square")

if __name__ == "__main__":
  main()