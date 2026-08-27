class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const set = new Set(nums)
        const answer = set.size !== nums.length
        return answer
    }
}
