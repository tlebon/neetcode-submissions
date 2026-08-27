class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const last = nums.length
        const hashMap = {}
        for (let i = 0; i < last; i++) {
            let diff = target - nums[i]
            let index = diff in hashMap
            if (index) {
                return [hashMap[diff], i]
            }
            hashMap[nums[i]] = i
        }


    }
}
