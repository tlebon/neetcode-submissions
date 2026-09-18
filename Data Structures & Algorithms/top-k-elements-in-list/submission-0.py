class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict= {}
        for x in nums:
            if x not in numdict:
                numdict[x]=1
            else:
                numdict[x]= numdict[x]+1

        numdictarr = numdict.items()
        return [x[0] for x in heapq.nlargest(k, numdictarr, key= lambda val: val[1])]