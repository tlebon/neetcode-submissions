class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false
        const table1 = {}
        const table2 = {}
        let answer = true
        for (let i of s) {
            if (table1[i]) {
                table1[i]++
            } else {
                table1[i] = 1
            }
        }
        for (let i of t) {
            if (table2[i]) {
                table2[i]++
            } else {
                table2[i] = 1
            }
        }
        let iterator = 0;
        Object.keys(table1).forEach((key) => {
            if (table1[key] !== table2[key]) {
                answer = false
            }
            iterator += 1
            if (iterator === Object.keys(table1).length - 1 && table1[key] === table2[key]) {
                answer = true
            }
        }
        )
        return answer
    }

}
