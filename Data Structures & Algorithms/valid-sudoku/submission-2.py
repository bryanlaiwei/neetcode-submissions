class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subBoxDict = {
            (3, 3): set(),
            (3, 6): set(),
            (3, 9): set(),
            (6, 3): set(),
            (6, 6): set(),
            (6, 9): set(),
            (9, 3): set(),
            (9, 6): set(),
            (9, 9): set(),
        }
        colDict = {
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set(),
            9: set(),
        }

        for row in range(0, 9):
            rowSet = set()
            for col in range(0, 9):
                num = board[row][col]
                if num == ".": continue

                if num not in rowSet: rowSet.add(num)
                else: return False

                if num not in colDict[col + 1]: colDict[col + 1].add(num)
                else: return False

                tp = ((row // 3) * 3 + 3, (col // 3) * 3 + 3)
                if num not in subBoxDict[tp]: subBoxDict[tp].add(num)
                else: return False
        
        return True

        