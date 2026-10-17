class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        low = 0
        high = 0
        for n in range(l):
            if numbers[low] + numbers[l - 1 - high] > target:
                high = high + 1
            elif numbers[low] + numbers[l - 1 - high] < target:
                low = low + 1
            else:
                return [low+1, l - high]