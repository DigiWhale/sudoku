what can you do to a sodoku board?

next meeting: saturday at 11AM CST
# lu?
# def find_numbers_in_a_column
#     - identify which numbers still need to be added
#     - return list of [numbers_to_be_added]
#     - return list of [numbers_already_there]
#lu?
# def find_numbers_in_a_row
#     - identify which numbers still need to be added
#     - return list of [numbers_to_be_added]
#     - return list of [numbers_already_there]
#     # for i in range(len(list[0])):
#         #if
#lu?
# def find_numbers_in_a_box
#     - identify which numbers still need to be added
#     - return list of [numbers_to_be_added]
#     - return list of [numbers_already_there]
#Andrew
def insert_a_value_into_a_square(self, row, column, value_to_insert):
    board[array_index][index_in_array] = value_to_insert #assigns a position on the board
    return board[array_index] #returns an array of the row that has been modified

#Andrew
def check_box(self, box, number_to_find) 
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
# # def print_board

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


#boggle solution
# import random
# class BoggleBoard:
#   #obj for dice
#   dice = [["AAEEGN", "ELRTTY", "AOOTTW", "ABBJOO"], 
#           ["EHRTVW", "CIMOTU", "DISTTY", "EIOSST"],
#           ["DELRVY", "ACHOPS", ["H", "I", "M", "N", "Qu", "U"], "EEINSU"],
#           ["EEGHNW", "AFFKPS", "HLNNRZ", "DEILRX"]]
#   #init empty board and print it
#   def __init__(self):
#     self.board = [['_', '_', '_', '_'], 
#                   ['_', '_', '_', '_'], 
#                   ['_', '_', '_', '_'], 
#                   ['_', '_', '_', '_']]
#     self.print_board()

#   #add a random outcome from the tice to the board
#   def shake(self):
#     for board_length in range(0, len(self.board)):
#       for board_width in range(0, len(self.board[0])):
#         self.board[board_length][board_width] = self.dice[board_length][board_width][random.randint(0, 5)]
#     self.print_board()
#   #print the board, watching out for Qu
#   def print_board(self):
#     for board_length in range(0, len(self.board)):
#       for board_width in range(0, len(self.board[0])):
#         print(self.board[board_length][board_width], ' ', end = "")
#         if self.board[board_length][board_width] != 'Qu':
#           print(' ', end  ='')
#       print('')

#   #check if a word is in the board
#   def include_word(self, word):
#     #returns a list of xy locations of the letters are on the board in a list
#     def find_next_letter(letter):
#           matching_indexes = []
#           for row in range(0, len(self.board)):
#             for column in range(0, len(self.board[0])):
#               # print(self.board[row][column])
#               if self.board[row][column] == letter.upper():
#                 # print(row, column)
#                 matching_indexes.append([row, column])
#           return matching_indexes

#     #returns true if any string of characters in order are close enough to match
#     def do_letters_line_up(matching_letters):
#       #makes sure all the letters have some locations on the board before start
#       if not len(matching_letters_indexes) >= len(word):
#         return False
#       if len(matching_letters) == 1:
#         # print(matching_letters)
#         # print(matching_letters_indexes)
#         return True
#       for letter in matching_letters[0]:
#         for second_letter in matching_letters[1]:
#           if abs(letter[0] - second_letter[0]) <= 1 and abs(letter[1] - second_letter[1]) <= 1:
#             next_matching_letters = matching_letters
#             #for loop to take out board spots already used from other lists, in case of multiple same letters
#             for each_list in next_matching_letters:
#               for every_list in each_list:
#                 if every_list == letter:
#                   each_list.remove(every_list)
#             return do_letters_line_up(next_matching_letters[1:])
#       return False

#     #fill list with board locations of each letter
#     matching_letters_indexes = []
#     for letter in word:
#       newlist = find_next_letter(letter)
#       #keep empty lists from getting in
#       if len(newlist) > 0:
#         matching_letters_indexes.append(newlist)

#     print(do_letters_line_up(matching_letters_indexes))
#     # print(matching_letters_indexes)


    



# newgame = BoggleBoard()
# newgame.shake()

# print('type "exit" to exit loop')
# guess = input("guess a word in the board, any size: ")
# while(guess != 'exit'):
#   newgame.include_word(guess)
#   guess = input("guess a word in the board, any size: ")