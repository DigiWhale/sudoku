import re
import random
class SudokuSolver:
  def __init__(self, board_string, original=True):
    self.original_string = board_string
    self.board_list_of_lists = self.string_to_list_of_lists(board_string)
    self.box_index_table = self.fill_box_index_table()
    self.taken_row_values = self.list_of_lists_rows_taken_numbers()
    self.taken_column_values = self.list_of_lists_columns_taken_numbers()
    self.taken_box_values = self.list_of_lists_squares_taken_numbers()
    self.taken_values_at_index_dict = self.dictionary_of_board_indexes_available_values()
    self.dictionary_of_indexes_not_possible_lists = self.create_dictionary_of_indexes_not_possible_lists()
    self.add_for_sure_values_to_board(self.board_list_of_lists)
    self.total_loops_ran = 0 #delete this

    if not self.check_if_board_passes(self.board_list_of_lists) and original:
      self.fill_board_and_solve()
    if original:
      self.print_board()
      # print(self.dictionary_of_indexes_not_possible_lists)
      print(self.check_if_board_passes(self.board_list_of_lists))
      # print("the total loops were " + str(self.total_loops_ran))
    # return self.check_if_board_passes(self.board_list_of_lists)

  def solve(self):
    pass

  def board(self):
    pass

  def fill_board_and_solve(self):
    new_solver = SudokuSolver(self.original_string, original=False)
    attempts = 0
    while(not new_solver.check_if_board_passes(new_solver.board_list_of_lists) and attempts < 6000):
      new_solver = SudokuSolver(self.original_string, original=False)
      attempts += 1
      step = attempts // 100
      for i in range(step):
        random_key = random.choice(list(new_solver.taken_values_at_index_dict.keys()))
        random_key_list = new_solver.taken_values_at_index_dict[random_key]
        if len(random_key_list) != 9:
          possible_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
          for not_possible_value in random_key_list:
            possible_values.remove(not_possible_value)
          for value in possible_values:
            new_solver.board_list_of_lists[int(random_key[0])][int(random_key[1])] = value
            new_solver.refresh()
    self.board_list_of_lists = new_solver.board_list_of_lists
          
  def refresh(self):
    self.taken_row_values = self.list_of_lists_rows_taken_numbers()
    self.taken_column_values = self.list_of_lists_columns_taken_numbers()
    self.taken_box_values = self.list_of_lists_squares_taken_numbers()
    self.taken_values_at_index_dict = self.dictionary_of_board_indexes_available_values()
    self.add_for_sure_values_to_board(self.board_list_of_lists)

  def create_dictionary_of_indexes_not_possible_lists(self):
    return_dictionary = {}
    for box, box_list in self.taken_values_at_index_dict.items():
      new_key = str(len(box_list))
      if new_key in return_dictionary:
        return_dictionary[new_key].append(box)
      else:
        return_dictionary[new_key] = [box]
    return return_dictionary
  
  def add_for_sure_values_to_board(self, list_of_lists):
    for cycle in range(10):
      #inserts value if only one missing from list
      if '8' in self.dictionary_of_indexes_not_possible_lists.keys():
        if len(self.dictionary_of_indexes_not_possible_lists['8']) > 0:
          for i in self.dictionary_of_indexes_not_possible_lists['8']:
            for j in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
              if j not in self.taken_values_at_index_dict[i]:
                self.board_list_of_lists[int(i[0])][int(i[1])] = j
                self.refresh()
      #if only square with possibility with value in box, then it must be that value!!!
      for value in range(1, 10, 1):
        for box in self.box_index_table:
          squares_without_value = []
          for square in self.box_index_table[box]:
            if str(value) not in self.taken_values_at_index_dict[square]:
              squares_without_value.append(square)
          if len(squares_without_value) == 1:
            square = squares_without_value[0]
            self.board_list_of_lists[int(square[0])][int(square[1])] = str(value)
            # self.print_board()
            self.taken_row_values = self.list_of_lists_rows_taken_numbers()
            self.taken_column_values = self.list_of_lists_columns_taken_numbers()
            self.taken_box_values = self.list_of_lists_squares_taken_numbers()
            self.taken_values_at_index_dict = self.dictionary_of_board_indexes_available_values()
            return self.add_for_sure_values_to_board(list_of_lists)
      if self.check_if_board_passes(self.board_list_of_lists) == True:
        break

  def check_if_board_passes(self, list_of_lists):
    for row in list_of_lists:
      for square in row:
        if square == '0':
          return False
      checked_list = list(dict.fromkeys(row))
      if len(row) != len(checked_list):
        return False
    for index, row in enumerate(list_of_lists):
      column = []
      for i in range(len(list_of_lists)):
        column.append(list_of_lists[index][i])
      checked_column = list(dict.fromkeys(column))
      if len(column) != len(checked_column):
        return False
    for j in range(0, 70, 30):
      for i in range(0, 7, 3):
        list_of_box_values = self.return_values_in_a_box(str(j+i).zfill(2), list_of_lists)
        checked_list_of_box_values = list(dict.fromkeys(list_of_box_values))
        if len(list_of_box_values) != len(checked_list_of_box_values):
          return False
    return True


  def dictionary_of_board_indexes_available_values(self):
    dictionary = {}
    for row_index, row in enumerate(self.board_list_of_lists):
      for column_index, column in enumerate(row):
        xy_index = (str(row_index) + str(column_index)).zfill(2)
        if self.board_list_of_lists[row_index][column_index] == '0':
          row_taken_value_list = self.taken_row_values[row_index]
          column_taken_value_list = self.taken_column_values[column_index]
          box_taken_value_list = self.taken_box_values[self.find_box_of_index(xy_index)]
          all_taken_values_at_index_dublicates = row_taken_value_list + column_taken_value_list + box_taken_value_list
          all_taken_values_at_index = list(dict.fromkeys(all_taken_values_at_index_dublicates))
          dictionary[xy_index] = all_taken_values_at_index
        else:
          given_value_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
          # given_value_list.remove(self.board_list_of_lists[row_index][column_index])
          dictionary[xy_index] = given_value_list
    return dictionary

  def list_of_lists_squares_taken_numbers(self):
    return_list = []
    for box in range(9):
      return_list.append(self.non_zero_values_in_square(self.box_index_table[box][0]))
    return return_list

  def list_of_lists_columns_taken_numbers(self):
    return_list = []
    for column in range(len(self.board_list_of_lists[0])):
      return_list.append(self.non_zero_values_in_column(column))
    return return_list

  def list_of_lists_rows_taken_numbers(self):
    return_list = []
    for index, _row in enumerate(self.board_list_of_lists):
      return_list.append(self.non_zero_values_in_row(index))
    return return_list

  def string_to_list_of_lists(self, board_string):
    return_list = []
    rows = re.findall(r"\d{9}", board_string)
    for row in rows:
      adding_list = []
      adding_list[:0] = row
      return_list.append(adding_list)
    return return_list
  
  def print_board(self):
    for index1, row in enumerate(self.board_list_of_lists):
      if index1 == 0 or index1 == 3 or index1 == 6:
        print('-' * 21)
      for index, char in enumerate(row):
        print(char, '', end='')
        if index == 2 or index == 5:
          print('| ', end = '')
      print('')
      if index1 == 8:
          print('-' * 21)

  def non_zero_values_in_row(self, row_index):
    return_list = self.filter_element_from_list(self.board_list_of_lists[row_index], '0')
    return return_list

  def non_zero_values_in_column(self, column_index):
    return_list = []
    for row in self.board_list_of_lists:
      if row[column_index] != '0':
        return_list.append(row[column_index])
    return return_list
  
  #square_index should be [x, x] both ints
  #returns values taking in the square
  def non_zero_values_in_square(self, square_index):
    square_index = (str(square_index[0]) + str(square_index[1])).zfill(2)
  
    box = self.find_box_of_index(square_index)

    return_list = []
    for three_by_three_index in self.box_index_table[box]:
      row_value = int(three_by_three_index[0])
      char_value = int(three_by_three_index[1])
      if self.board_list_of_lists[row_value][char_value] != '0':
        return_list.append(self.board_list_of_lists[row_value][char_value])

    return return_list

  def return_values_in_a_box(self, square_index, list_of_lists):
    square_index = (str(square_index[0]) + str(square_index[1])).zfill(2)
    box = self.find_box_of_index(square_index)

    return_list = []
    for three_by_three_index in self.box_index_table[box]:
      row_value = int(three_by_three_index[0])
      char_value = int(three_by_three_index[1])
      return_list.append(self.board_list_of_lists[row_value][char_value])

    return return_list
  
  # index should be two character string
  def find_box_of_index(self, index):
    box = ''
    for each_box in self.box_index_table:
      if index in self.box_index_table[each_box]:
        box = each_box
        break
    return box

  def fill_box_index_table(self):
    boxes = {}
    box_center = [1, 1]
    box_number = 0
    for _row_of_boxes in range(3):
      for _each_box in range(3):
        box_list = []
        for i in range(-1, 2):
          box_list.append(str(box_center[0] + i) + str(box_center[1] - 1))
          box_list.append(str(box_center[0] + i) + str(box_center[1]))
          box_list.append(str(box_center[0] + i) + str(box_center[1] + 1))
        boxes[box_number] = box_list
        box_number += 1
        box_center[1] += 3
      box_center[0] += 3
      box_center[1] -= 9
    return boxes

  def filter_element_from_list(self, alist, filtered_value):
    return_list = []
    for i in alist:
      if i != filtered_value:
        return_list.append(i)
    return return_list


# puzzle = SudokuSolver("003020600900305001001806400008102900700000008006708200002609500800203009005010300")
# puzzle.print_board()
#print(puzzle.non_zero_values_in_square([0, 2]))
#print(puzzle.non_zero_values_in_column(0))
#print(puzzle.non_zero_values_in_row(3))
#print(puzzle.board_list_of_lists)
# print(puzzle.box_index_table)
#print(puzzle.taken_row_values)
#print(puzzle.taken_column_values)
#print(puzzle.taken_box_values)
# for i in puzzle.taken_values_at_index_dict:
#   print(i ,puzzle.taken_values_at_index_dict[i])
#puzzle.fill_board_and_solve()
# The file has newlines at the end of each line, so we call
# String#chomp to remove them.
# game = SudokuSolver(board_string)
# # Remember: this will just fill out what it can and not "guess"
# game.solve
# print(game.board)
#square_index should be [x, x] both ints
#returns values taking in the square

# puzzle2 = SudokuSolver("483921657967345821251876493548132976729564138136798245372689514814253769695417382")
# puzzle2.print_board()
# print(puzzle2.check_if_board_passes(puzzle2.board_list_of_lists))


############ TEST CASES - SHOULD ALL RETURN TRUE ##########################################################################

puzzle1 = SudokuSolver("003020600900305001001806400008102900700000008006708200002609500800203009005010300")
puzzle2 = SudokuSolver("200080300060070084030500209000105408000000000402706000301007040720040060004010003")
puzzle3 = SudokuSolver("000000907000420180000705026100904000050000040000507009920108000034059000507000000")
puzzle4 = SudokuSolver("030050040008010500460000012070502080000603000040109030250000098001020600080060020")
puzzle5 = SudokuSolver("020810740700003100090002805009040087400208003160030200302700060005600008076051090")
puzzle6 = SudokuSolver("100920000524010000000000070050008102000000000402700090060000000000030945000071006")
puzzle7 = SudokuSolver("043080250600000000000001094900004070000608000010200003820500000000000005034090710")
puzzle8 = SudokuSolver("480006902002008001900370060840010200003704100001060049020085007700900600609200018")
puzzle9 = SudokuSolver("000900002050123400030000160908000000070000090000000205091000050007439020400007000")
puzzle10 = SudokuSolver("001900003900700160030005007050000009004302600200000070600100030042007006500006800")
puzzle11 = SudokuSolver("000125400008400000420800000030000095060902010510000060000003049000007200001298000")
puzzle12 = SudokuSolver("062340750100005600570000040000094800400000006005830000030000091006400007059083260")
puzzle13 = SudokuSolver("300000000005009000200504000020000700160000058704310600000890100000067080000005437")
puzzle14 = SudokuSolver("630000000000500008005674000000020000003401020000000345000007004080300902947100080")
puzzle15 = SudokuSolver("000020040008035000000070602031046970200000000000501203049000730000000010800004000")
puzzle16 = SudokuSolver("361025900080960010400000057008000471000603000259000800740000005020018060005470329")
puzzle17 = SudokuSolver("050807020600010090702540006070020301504000908103080070900076205060090003080103040")
puzzle18 = SudokuSolver("080005000000003457000070809060400903007010500408007020901020000842300000000100080")
puzzle19 = SudokuSolver("003502900000040000106000305900251008070408030800763001308000104000020000005104800")
puzzle20 = SudokuSolver("000000000009805100051907420290401065000000000140508093026709580005103600000000000")
puzzle21 = SudokuSolver("020030090000907000900208005004806500607000208003102900800605007000309000030020050")
puzzle22 = SudokuSolver("005000006070009020000500107804150000000803000000092805907006000030400010200000600")
puzzle23 = SudokuSolver("040000050001943600009000300600050002103000506800020007005000200002436700030000040")
puzzle24 = SudokuSolver("004000000000030002390700080400009001209801307600200008010008053900040000000000800")
puzzle25 = SudokuSolver("360020089000361000000000000803000602400603007607000108000000000000418000970030014")
puzzle26 = SudokuSolver("500400060009000800640020000000001008208000501700500000000090084003000600060003002")
puzzle27 = SudokuSolver("007256400400000005010030060000508000008060200000107000030070090200000004006312700")
puzzle28 = SudokuSolver("000000000079050180800000007007306800450708096003502700700000005016030420000000000")
puzzle29 = SudokuSolver("030000080009000500007509200700105008020090030900402001004207100002000800070000090")
puzzle30 = SudokuSolver("200170603050000100000006079000040700000801000009050000310400000005000060906037002")
puzzle31 = SudokuSolver("000000080800701040040020030374000900000030000005000321010060050050802006080000000")
puzzle32 = SudokuSolver("000000085000210009960080100500800016000000000890006007009070052300054000480000000")
puzzle33 = SudokuSolver("608070502050608070002000300500090006040302050800050003005000200010704090409060701")
puzzle34 = SudokuSolver("050010040107000602000905000208030501040070020901080406000401000304000709020060010")
puzzle35 = SudokuSolver("053000790009753400100000002090080010000907000080030070500000003007641200061000940")
puzzle36 = SudokuSolver("006080300049070250000405000600317004007000800100826009000702000075040190003090600")
puzzle37 = SudokuSolver("005080700700204005320000084060105040008000500070803010450000091600508007003010600")
puzzle38 = SudokuSolver("000900800128006400070800060800430007500000009600079008090004010003600284001007000")
puzzle39 = SudokuSolver("000080000270000054095000810009806400020403060006905100017000620460000038000090000")
puzzle40 = SudokuSolver("000602000400050001085010620038206710000000000019407350026040530900020007000809000")
puzzle41 = SudokuSolver("000900002050123400030000160908000000070000090000000205091000050007439020400007000")
puzzle42 = SudokuSolver("380000000000400785009020300060090000800302009000040070001070500495006000000000092")
puzzle43 = SudokuSolver("000158000002060800030000040027030510000000000046080790050000080004070100000325000")
puzzle44 = SudokuSolver("010500200900001000002008030500030007008000500600080004040100700000700006003004050")
puzzle45 = SudokuSolver("080000040000469000400000007005904600070608030008502100900000005000781000060000010")
puzzle46 = SudokuSolver("904200007010000000000706500000800090020904060040002000001607000000000030300005702")
puzzle47 = SudokuSolver("000700800006000031040002000024070000010030080000060290000800070860000500002006000")
puzzle48 = SudokuSolver("001007090590080001030000080000005800050060020004100000080000030100020079020700400")
puzzle49 = SudokuSolver("000003017015009008060000000100007000009000200000500004000000020500600340340200000")
puzzle50 = SudokuSolver("300200000000107000706030500070009080900020004010800050009040301000702000000008006")