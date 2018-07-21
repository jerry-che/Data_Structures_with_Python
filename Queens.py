#  File: Queens.py

#  Description: code that solves 

#  Student Name: Jerry Che

#  Student UT EID:jc78222

#  Partner Name:Terry Woodward Jr

#  Partner UT EID: tgw466

#  Course Name: CS 313E

#  Unique Number: 86350

#  Date Created: 07/16/18

#  Date Last Modified: 07/20/18


class Queens:
    #initilizer to check for the
    def __init__(self, n):
        self.n = n
        self.solutions = 0

    def solve(self):
        positions = [-1] * self.n
        self.recursiveSolve(positions, 0)
        print("There are", self.solutions, "solutions for a",str(self.n),"x",str(self.n),"board")

    def recursiveSolve(self, pos, row):
        if row == self.n:
            self.printBoard(pos)
            self.solutions += 1
        else:
            for col in range(self.n):
                if self.isValid(pos, row, col):
                    pos[row] = col
                    self.recursiveSolve(pos,row + 1)


    def isValid(self, pos, row, col):
        for i in range(row):
            if pos[i] == col or \
                pos[i] - i == col - row or \
                pos[i] + i == col + row:

                return False
        return True

    def printBoard(self, pos):
        for row in range(self.n):
            line = ""
            for column in range(self.n):
                if pos[row] == column:
                    line += "Q "
                else:
                    line += "* "
            print(line)
        print("\n")


def main():
    board_size = int(input("Enter the board size:"))
    while (board_size < 1 or board_size > 8):
        board_size = int(input("Enter the board size:"))

    chess_board = Queens(board_size)
    chess_board.solve()




if __name__ == "__main__":
    # execute only if run as a script
    main()

