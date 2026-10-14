class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        last = len(numbers) - 1
        for i, x in enumerate(numbers):
            if x + numbers[last] < target:
                continue
            for j, y in enumerate(numbers[-1::-1]):
                if y + numbers[i] > target:
                    continue
                if x + y == target:
                    return [i + 1, len(numbers) - j]
