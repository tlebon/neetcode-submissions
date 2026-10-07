class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isValid = True
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i, rows in enumerate(board):
            seen = set()
            for j, item in enumerate(rows):
                if item == ".":
                    continue
                if item in seen:
                    return False
                seen.add(item)

                if item in cols[j]:
                    return False
                cols[j].add(item)

                if item in boxes[i // 3 + (3 * (j // 3))]:
                    return False
                else:
                    boxes[i // 3 + (3 * (j // 3))].add(item)

        return isValid
