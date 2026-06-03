class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */

    groupAnagrams(strs) {
        let res = {};

        for(let word of strs){
            let count = new Array(26).fill(0);

            for(let char of word){
                count[char.charCodeAt(0) - "a".charCodeAt(0)]++
            }

            let key = count.join("#");
            if(!res[key]){
                res[key] = []
            }

            res[key].push(word)
        }

        return Object.values(res)

    }
}
