def convert_board_string_into_array_of_array(board_string=self.board_string, step=9):
    board_array =  [board_string[i::step] for i in range(step)] #iterate through string and grab every ninth character
    for i in range(len(board_array)):
        for j in range(len(board_array[i])):
            board_array[i] = list(board_array[i]) # turns board array into 9 arrays of single string
            board_array[i][j] = int(board_array[i][j]) #breaks string into individual arrays and converts to int()
    return board_array #returns and array of arrays representing the board_array
