class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i, row in enumerate(board):
            seen = set()
            for j, item in enumerate(row):
                if item == ".":
                    continue
                if item in seen:
                    return False
                seen.add(item)

                if item in cols[j]:
                    return False
                cols[j].add(item)
                box = boxes[i // 3 + (3 * (j // 3))]
                if item in box:
                    return False
                box.add(item)

        return True
