class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Step 1: Initialize collection structures for rows, columns, and 3x3 sub-boxes
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
         # Step 2: Iterate through each row from 0 to 8
        for r in range(9):
            # Step 3: Inerate through each column c from 0 to 8
            for c in range(9):
                # Step 4: Retrieve the character val
                val = board[r][c]
                # Step 5: Skip empty cells
                if val == '.':
                    continue
                # Step 6: Check if val already in its respective row, column, or sub-box
                box_key = (r //3, c // 3)
                if (
                    val in rows[r]
                    or val in cols[c]
                    or val in boxes[box_key]
                ):
                    return False
                
                # Step 7: Add aval to the tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)
        # Step 8: Return True if no duplicats violtions were found
        return True
            