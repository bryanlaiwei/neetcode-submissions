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

                if num not in rowSet: 
                    rowSet.add(num)
                else: 
                    print("failed row")
                    print(rowSet)
                    return False

                if num not in colDict[col + 1]: 
                    colDict[col + 1].add(num)
                else: 
                    print("failed col")
                    return False

                tpRow = (row // 3) * 3 + 3
                tpCol = (col // 3) * 3 + 3
                tp = (tpRow, tpCol)
                if num not in subBoxDict[tp]: 
                    subBoxDict[tp].add(num)
                else: 
                    print("failed 3x3")
                    return False
        
        return True

        