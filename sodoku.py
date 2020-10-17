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

def insert_a_value_into_a_square(row, column, value_to_insert):
    board[array_index][index_in_array] = value_to_insert #assigns a position on the board
    return board[array_index] #returns an array of the row that has been modified


def find_empty_cell(board_array):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return (row, column)

def check_valid_placement(row=0, column=0, number_to_check=0): #rows and columns are indexed from the top left, Row 0 is on top, row 9 is on bottom
    #columns start on the left at column 0 and end on the right at column 9
    #check row and column
    for i in range(9):
        if board[row][i] == number_to_check or board[i][column] == number_to_check:
            return False

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