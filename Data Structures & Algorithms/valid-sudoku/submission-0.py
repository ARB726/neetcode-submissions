class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        column = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9): # for rows 

            for j in range(9): # for columns

                currentValue = board [i][j]

                if currentValue == ".":
                    continue

                if currentValue not in rows[i] and currentValue not in column[j] and currentValue not in boxes[i//3,j//3]: # to do
                    rows[i].add(currentValue)
                    column[j].add(currentValue)
                    boxes[i//3,j//3].add(currentValue)
                    # print("set of row",rows)
                    # print("set of col",columns)
                    # print("set of boxes",boxes)
                else:
                    return False
        return True







"""
NOTES:

- Three sets
            -> one for row
            -> one for column
            -> one for 3*3 box

- create a board that is a 2d list that stores column and rows    
"""