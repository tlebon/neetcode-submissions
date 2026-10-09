class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        short = set(nums)
        seq = []
        longest = 0
        for x in short:
            seq = [x]
            if x - 1 in short:
                continue
            else:
                for y in range(1,len(short)):
                    if x + y in short:
                        seq.append(x+y)
                    else: 
                        break
                if longest < len(seq):
                    longest = len(seq)
        return longest
