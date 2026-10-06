class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suf = []
        result = [1 for x in range(len(nums))]

        for i, x in enumerate(nums):
            if i == 0:
                pre.append(nums[i])
                suf.append(nums[len(nums) - 1])

            else:
                pre.append(pre[i - 1] * nums[i])
                suf.append(suf[i - 1] * nums[len(nums) - i - 1])
        suf.reverse()
        # print(pre, suf)

        for i in range(len(result)):
            if i == 0:
                result[i] = suf[i + 1]
            elif i == len(result) - 1:
                result[i] = pre[i - 1]
            else:
                result[i] = pre[i - 1] * suf[i + 1]
        return result
