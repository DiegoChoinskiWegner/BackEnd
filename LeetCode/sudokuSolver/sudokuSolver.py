def solveSudoku(board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        possible_values_row = []
        possible_value_column = []
        possible_value_square = []
        
        ## rules

        ## List[0] = can't repeat values
#        for sublista in board:
#            pattern_values_temp = ["1","2","3","4","5","6","7","8","9"]
#            for item in sublista:
#                if item in pattern_values_temp:
#                    pattern_values_temp.remove(item)
#            print(pattern_values_temp)
        

        ### List[0[0], 1[0] ... ... ] cant respeat values
#        for coluna in zip(*board):
#            pattern_values_temp_columns = ["1","2","3","4","5","6","7","8","9"]
#            for item in coluna:
#                if item in pattern_values_temp_columns:
#                    pattern_values_temp_columns.remove(item)
#        
#            print(pattern_values_temp_columns)


        ### List[0[0,1,2], 1[0,1,2], 2[0,1,2] and ... ] cant repeat value
        i=0
        e=3
        for sublista in board[i:e]:
            pattern_values_temp_square = ["1","2","3","4","5","6","7","8","9"]
            square_values = []
            for item in sublista[i:e]:
                square_values.append(item)

            print(square_values)

                #if item in pattern_values_temp:
                #    pattern_values_temp.remove(item)
            #print(pattern_values_temp)

 


board_1 = [["5","3",".",".","7",".",".",".","."],
           ["6",".",".","1","9","5",".",".","."],
           [".","9","8",".",".",".",".","6","."],
           ["8",".",".",".","6",".",".",".","3"],
           ["4",".",".","8",".","3",".",".","1"],
           ["7",".",".",".","2",".",".",".","6"],
           [".","6",".",".",".",".","2","8","."],
           [".",".",".","4","1","9",".",".","5"],
           [".",".",".",".","8",".",".","7","9"]]

solveSudoku(board_1)