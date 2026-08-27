class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false
        const table = {}
        let answer;
        for (let i of s) {
            if (table[i]) {
                table[i]++
            } else {
                table[i] = 1
            }
        }
        for (let i of t) {
            if (table[i]) {
                table[i]--
            } else {
                table[i] = 1
            }
        }
        answer = Object.values(table).every((x) => x === 0)
        return answer
    }

}
