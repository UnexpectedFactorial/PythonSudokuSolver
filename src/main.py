
import csv
import numpy as np

def read_CSV_File_Into_Array():

    global numberArray
    numberArray = []

    fileFound=False

    try:
        x = open("input.csv")
        fileFound=True

    except IOError:
        print("Can't find file. Please create an input.csv file and insert your Sudoku puzzle.")
        fileFound=False
        input("Press Enter to Exit")
        exit()

    finally:
        if fileFound:
            print("File found..........processing")
            x.close()


    if fileFound:

        with open('input.csv', newline='') as csvfile:
            global inputNumbers
            inputNumbers = list(csv.reader(csvfile))

            conversion = np.array(inputNumbers)
            inputNumbers = conversion.astype(np.int) #converts the string array to a int array for the algorithm


def solve(grid): #recursive function
    find = find_empty(grid)
    if not find: #stops the function when there are no empty spaces left
        return True
    else:
        row, col = find

    for a in range(1,10): #goes from 1-9
        if valid(grid, a, (row, col)): #if its valid, replace the 0 with the valid number, basically solving it
            grid[row][col] = a

            if solve(grid): #calls itself to make it recursive
                return True

            grid[row][col] = 0 #resets the last value if it hits a deadend, backtracking portion of the algorithm

    return False


def valid(grid, num, pos):
    # row checking (horizontal)
    for a in range(len(grid[0])): # grabs from 0 - 8 in the array,
        if grid[pos[0]][a] == num and pos[1] != a: # checks the row for an identical number to the one that was just placed, ignores the one that was placed obviously.
            return False

    # Check column
    for a in range(len(grid)):
        if grid[a][pos[1]] == num and pos[0] != a: # checks the column for an identical number to the one that was just placed, ignores the one that was placed obviously.
            return False

    # Check box
    box_x = pos[1] // 3 # gets the position of the subgrid in the x axis
    box_y = pos[0] // 3# gets the position of the subgrid in the y axis

    for a in range(box_y*3, box_y*3 + 3):
        for b in range(box_x * 3, box_x*3 + 3): # puts the "cursor" at the first number in the subgrid
            if grid[a][b] == num and (a,b) != pos:
                return False

    return True


def print_board(grid): # prints out the sudoku board in the traditional format rather than the 2d array that the computer reads,
    for a in range(len(grid)): # for loops are to go through the each row in the array. For loops in python are written like this.
        if a % 3 == 0 and a != 0:
            print("- - - - - - - - - - - - - - ")

        for b in range(len(grid[0])):
            if b % 3 == 0 and b != 0:
                print(" | ", end="")

            if b == 8:
                print(grid[a][b])
            else:
                print(str(grid[a][b]) + " ", end="")


def find_empty(grid): # finds the next empty space which is defined by 0 in our case
    for a in range(len(grid)):
        for b in range(len(grid[0])):
            if grid[a][b] == 0:
                return (a, b)  # row,col for the solve function

    return None


read_CSV_File_Into_Array()

print("\n Your unsolved sudoku is:\n")
print_board(inputNumbers)

solve(inputNumbers)

print("\n Here is your solved puzzle:\n")
print_board(inputNumbers)

input("\n\nPress enter to exit")








