what can you do to a sodoku board?

next meeting: saturday at 11AM CST
# lu?
    def valid_board(self, num, pos):
        # ***** check row *****
        # loop though every column in the current row
        for i in range(len(self.board[0])):
            # does the current pos equal NUM(num is 1-9) and are we not in the position we just inserted
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False

        # ***** check column *****
        # loop through every row in the current column
        for i in range(len(self.board)):
            # is our current y-pos equal to num? and ignore posistion we just inserted
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False

        # ***** check 3x3 box *****
        # i dont know how to say this w/o writing a book
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def find_empty(self):
        # iterate through the rows
        for i in range(len(self.board)):
            # iterare through the indexes of each row (the columns)
            for j in range(len(self.board[0])):
                # if current location on board equals 0, return location in tuple (i,j)
                if self.board[i][j] == 0:
                    return (i, j)
        # return None if it can not find a blank sqaure
        return None

    def solve(self):
        # find an empty square using FIND_EMPTY function
        find = self.find_empty()
        # if it can not find an empty square return true BASE CASE
        if not find:
            return True
        else:
            row, col = find

        # loop through values 1-9
        for i in range(1, 10):
            # check if valid using VALID_BOARD
            if self.valid_board(i, (find)):
                # if it is valid, add it to board
                self.board[row][col] = i
                # now that we added to the board, run SOLVE on the new board
                if self.solve():
                    return True
                # reset last element we added, and run again
                self.board[row][col] = 0

        return False
 
#Andrew
def insert_a_value_into_a_square(self, row=0, column=0, value_to_insert=0):
    board[array_index][index_in_array] = value_to_insert #assigns a position on the board
    return board[array_index] #returns an array of the row that has been modified

#Andrew
def check_box(self, box=(0,0), number_to_find=0) 
    #box is a tupple of the start position of the upper left corner of the individual boxes 
    #box_1 = (0,0) box_2 = (0,3) box_3 = (0,6)
    #box_4 = (3,0) box_5 = (3,3) box_6 = (3,6) 
    #box_7 = (6,0) box_8 = (6,3) box_9 = (6,6)
    for i in range(3): #iterate over first 3 rows
        for j in range(3): #iterate over the first 3 columns
            if board[i+box[0]][j+box[1]] == n: #checks if number_to_find exists in a box
                return True # if it finds the number it returns true
            else:
                return False #else it returns false to indicate number is not in the box

#Andrew
def find_empty_cell(self, board_array):
    for row in range(9): #iterate through the row
        for column in range(9): #iterate through the column
            if board[row][column] == 0: #check for a 0
                return (row, column) #returns the row and column of the 0

#Andrew
def check_valid_placement(self, row=0, column=0, number_to_check=0): #rows and columns are indexed from the top left, Row 0 is on top, row 9 is on bottom
    #columns start on the left at column 0 and end on the right at column 9
    #check row and column
    for i in range(9):
        if board[row][i] == number_to_check or board[i][column] == number_to_check: #this checks if the number_to_check is the only number copy in the row and column
            return False #returns false if it finds a duplicate in that row or colunm
        else:
            return True #returns true if the number is unique to the row and column

# Augie
# # def generate_board_array(self, array)
# # outputs " "

# Augie
board_string = "619030040270061008000047621486302079000014580031009060005720806320106057160400030"

# def board_list(board_string):
#     board_list = [char for char in board_string]  
#     return board_list

# print(board_list(board_string))

# def make_board(board_string):
#     board_list = [char for char in board_string]
#     board_board = []
#     subarray = []
#     array = [board_string[i:i+9] for i in range(0, len(board_string), 9)]
#     board_board.append(array)
#     print(board_board)
#     print(make_board(board_string))

def parse_the_board_string(self, string)
    output self.board

def board_passes(self, board):
    returns if board passes or not

Standard variables-
    board = ---------------------
            4 8 3 | 9 2 1 | 6 5 7
            9 6 7 | 3 4 5 | 8 2 1
            2 5 1 | 8 7 6 | 4 9 3
            ---------------------
            5 4 8 | 1 3 2 | 9 7 6
            7 2 9 | 5 6 4 | 1 3 8
            1 3 6 | 7 9 8 | 2 4 5
            ---------------------
            3 7 2 | 6 8 9 | 5 1 4
            8 1 4 | 2 5 3 | 7 6 9
            6 9 5 | 4 1 7 | 3 8 2
            ---------------------
    board_string = "619030040270061008000047621486302079000014580031009060005720806320106057160400030"
    board_board = split.board_string when i % 9 = 0

    board_array = [[4, 8, 3, 9, 2, 1, 6, 5, 7],[9, 6, 7, 3, 4, 5, 8, 2, 1],[2, 5, 1, 8, 7, 6, 4, 9, 3],[5, 4, 8, 1, 3, 2, 9, 7, 6],[7, 2, 9, 5, 6, 4, 1, 3, 8],[1, 3, 6, 7, 9, 8, 2, 4, 5],[3, 7, 2, 6, 8, 9, 5, 1, 4],[8, 1, 4, 2, 5, 3, 7, 6, 9],[6, 9, 5, 4, 1, 7, 3, 8, 2]]

    box_1= (0,0)
    box_2= (0,3)
    box_3= (0,6)
    box_4= (3,0)
    box_5= (3,3)
    box_6= (3,6)
    box_7= (6,0)
    box_8= (6,3)
    box_8= (6,6)

# if you have a list of everything each cell CANNOT be, then when you have 8 numbers there, you know what it must be. 

# import re
# import random
# class SudokuSolver:
#   def __init__(self, board_string):
#     self.board_list_of_lists = self.string_to_list_of_lists(board_string)
#     self.box_index_table = self.fill_box_index_table()
#     self.taken_row_values = self.list_of_lists_rows_taken_numbers()
#     self.taken_column_values = self.list_of_lists_columns_taken_numbers()
#     self.taken_box_values = self.list_of_lists_squares_taken_numbers()
#     self.taken_values_at_index_dict = self.dictionary_of_board_indexes_available_values()
#     self.proven_boards = []

#   def solve(self):
#     pass

#   def board(self):
#     pass

#   def fill_board_and_solve(self):
#     board_list_of_lists_original_values = self.board_list_of_lists
#     for list_size in range(7, 0, -1):
#       for key, value in self.taken_values_at_index_dict.items():
#         if len(value) >= list_size:
#           available_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#           for i in self.taken_values_at_index_dict[key]:
#             available_values.remove(i)
#           if len(available_values) == 0:
#             self.board_list_of_lists = board_list_of_lists_original_values
#             self.fill_board_and_solve()
#             return
#           # print(' values that were taken were:')
#           # print(self.taken_values_at_index_dict[key])
#           input_choice = random.choice(available_values)
#           # print("input value: " + input_choice + " at location " + key[0] + key[1])
#           self.board_list_of_lists[int(key[0])][int(key[1])] = input_choice
#           self.taken_row_values = self.list_of_lists_rows_taken_numbers()
#           self.taken_column_values = self.list_of_lists_columns_taken_numbers()
#           self.taken_box_values = self.list_of_lists_squares_taken_numbers()
#           self.taken_values_at_index_dict = self.dictionary_of_board_indexes_available_values()
#           #######################################################################################
#           # self.print_board()
#           # for i in self.taken_values_at_index_dict:
#           #   print(i ,self.taken_values_at_index_dict[i])
#           # x = input('')
#           ######################################################################################
#     if self.check_if_board_passes(self.board_list_of_lists):
#       self.proven_boards.append(self.board_list_of_lists)
#       print(self.proven_boards)
#     else:
#       self.board_list_of_lists = board_list_of_lists_original_values
#       self.fill_board_and_solve()

#   def check_if_board_passes(self, list_of_lists):
#     for row in list_of_lists:
#       checked_list = list(dict.fromkeys(row))
#       if len(row) != len(checked_list):
#         return False
#     for index, row in enumerate(list_of_lists):
#       column = []
#       for i in range(len(list_of_lists)):
#         column.append(list_of_lists[index][i])
#       checked_column = list(dict.fromkeys(column))
#       if len(column) != len(checked_column):
#         return False
#     for j in range(0, 70, 30):
#       for i in range(0, 7, 3):
#         list_of_box_values = self.return_values_in_a_box(str(j+i).zfill(2), list_of_lists)
#         checked_list_of_box_values = list(dict.fromkeys(list_of_box_values))
#         if len(list_of_box_values) != len(checked_list_of_box_values):
#           return False
#     return True

#   def dictionary_of_board_indexes_available_values(self):
#     dictionary = {}
#     for row_index, row in enumerate(self.board_list_of_lists):
#       for column_index, column in enumerate(row):
#         xy_index = (str(row_index) + str(column_index)).zfill(2)
#         if self.board_list_of_lists[row_index][column_index] == '0':
#           row_taken_value_list = self.taken_row_values[row_index]
#           column_taken_value_list = self.taken_column_values[column_index]
#           box_taken_value_list = self.taken_box_values[self.find_box_of_index(xy_index)]
#           all_taken_values_at_index_dublicates = row_taken_value_list + column_taken_value_list + box_taken_value_list
#           all_taken_values_at_index = list(dict.fromkeys(all_taken_values_at_index_dublicates))
#           dictionary[xy_index] = all_taken_values_at_index
#         else:
#           given_value_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#           given_value_list.remove(self.board_list_of_lists[row_index][column_index])
#           dictionary[xy_index] = given_value_list
#     return dictionary

#   def list_of_lists_squares_taken_numbers(self):
#     return_list = []
#     for box in range(9):
#       return_list.append(self.non_zero_values_in_square(self.box_index_table[box][0]))
#     return return_list

#   def list_of_lists_columns_taken_numbers(self):
#     return_list = []
#     for column in range(len(self.board_list_of_lists[0])):
#       return_list.append(self.non_zero_values_in_column(column))
#     return return_list

#   def list_of_lists_rows_taken_numbers(self):
#     return_list = []
#     for index, _row in enumerate(self.board_list_of_lists):
#       return_list.append(self.non_zero_values_in_row(index))
#     return return_list

#   def string_to_list_of_lists(self, board_string):
#     return_list = []
#     rows = re.findall(r"\d{9}", board_string)
#     for row in rows:
#       adding_list = []
#       adding_list[:0] = row
#       return_list.append(adding_list)
#     return return_list
  
#   def print_board(self):
#     for index1, row in enumerate(self.board_list_of_lists):
#       if index1 == 0 or index1 == 3 or index1 == 6:
#         print('-' * 21)
#       for index, char in enumerate(row):
#         print(char, '', end='')
#         if index == 2 or index == 5:
#           print('| ', end = '')
#       print('')
#       if index1 == 8:
#           print('-' * 21)

#   def non_zero_values_in_row(self, row_index):
#     return_list = self.filter_element_from_list(self.board_list_of_lists[row_index], '0')
#     return return_list

#   def non_zero_values_in_column(self, column_index):
#     return_list = []
#     for row in self.board_list_of_lists:
#       if row[column_index] != '0':
#         return_list.append(row[column_index])
#     return return_list
  
#   #square_index should be [x, x] both ints
#   #returns values taking in the square
#   def non_zero_values_in_square(self, square_index):
#     square_index = (str(square_index[0]) + str(square_index[1])).zfill(2)
  
#     box = self.find_box_of_index(square_index)

#     return_list = []
#     for three_by_three_index in self.box_index_table[box]:
#       row_value = int(three_by_three_index[0])
#       char_value = int(three_by_three_index[1])
#       if self.board_list_of_lists[row_value][char_value] != '0':
#         return_list.append(self.board_list_of_lists[row_value][char_value])

#     return return_list

#   def return_values_in_a_box(self, square_index, list_of_lists):
#     square_index = (str(square_index[0]) + str(square_index[1])).zfill(2)
#     box = self.find_box_of_index(square_index)

#     return_list = []
#     for three_by_three_index in self.box_index_table[box]:
#       row_value = int(three_by_three_index[0])
#       char_value = int(three_by_three_index[1])
#       return_list.append(self.board_list_of_lists[row_value][char_value])

#     return return_list
  
#   # index should be two character string
#   def find_box_of_index(self, index):
#     box = ''
#     for each_box in self.box_index_table:
#       if index in self.box_index_table[each_box]:
#         box = each_box
#         break
#     return box

#   def fill_box_index_table(self):
#     boxes = {}
#     box_center = [1, 1]
#     box_number = 0
#     for _row_of_boxes in range(3):
#       for _each_box in range(3):
#         box_list = []
#         for i in range(-1, 2):
#           box_list.append(str(box_center[0] + i) + str(box_center[1] - 1))
#           box_list.append(str(box_center[0] + i) + str(box_center[1]))
#           box_list.append(str(box_center[0] + i) + str(box_center[1] + 1))
#         boxes[box_number] = box_list
#         box_number += 1
#         box_center[1] += 3
#       box_center[0] += 3
#       box_center[1] -= 9
#     return boxes

#   def filter_element_from_list(self, alist, filtered_value):
#     return_list = []
#     for i in alist:
#       if i != filtered_value:
#         return_list.append(i)
#     return return_list
