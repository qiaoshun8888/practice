'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''


class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    choices = [str(i) for i in range(1, 10)]

    def get_col(self, col):
        res = []
        for i in range(9):
            res.append(self.board[i][col])
        return res

    def get_row(self, row):
        return self.board[row]

    def set_value(row, col, value):
        self.board[row][col] = value

    def valid(self, i, j):
        pass

    def get_emptiest(self):
        emptiest_row = float('inf')
        emptiest_col = float('inf')
        row = 0
        col = 0
        for i in range(9):
            empty_count = self.get_row(i).count('.')
            # print empty_count
            if empty_count < emptiest_row:
                emptiest_row = empty_count
                row = i

        for i in range(9):
            empty_count = self.get_col(i).count('.')
            # print empty_count
            if empty_count < emptiest_col:
                emptiest_col = empty_count
                col = i

        if emptiest_row > emptiest_col:
            return col, 'col'
        else:
            return row, 'row'

    def solveSudoku(self, board):
        self.board = board
        print self.get_emptiest()
        # while self.valid() and self.not_complete():
        #     col, row = None, None
        #     col_or_row, number = self.get_emptiest()
        #     if col_or_row == 'col':
        #         col = self.get_col(number)
        #         for row, i in enumerate(col):
        #             if i == '.':
        #                 for j in self.choices:
        #                     if j not in col:
        #                         self.set_value(row, col, j)
        #                         # next
        #     else:
        #         row = self.get_row(number)
        #         for col, i in enumerate(row):
        #             if i == '.':
        #                 for j in self.choices:
        #                     if j not in row:
        #                         self.set_value(row, col, j)
        #                         # next



def main():
    s = Solution()
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ]
    s.solveSudoku(board)

if __name__ == '__main__':
    main()
