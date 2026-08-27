class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const hash = {}
        strs.forEach(x => {
            let sort = [...x].sort()
            if (sort in hash) {
                hash[sort].push(x)
            } else hash[sort] = [x]
        })
        return Object.values(hash)
    }
}
