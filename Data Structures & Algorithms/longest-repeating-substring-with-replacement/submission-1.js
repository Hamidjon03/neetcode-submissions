class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        let count = new Map();
        let res = 0;
        let maxF = 0;
        let left = 0;

        for(let right = 0; right < s.length; right++){
            count.set(s[right], (count.get(s[right]) || 0) + 1);
            maxF = Math.max(maxF, count.get(s[right]));

            while(right - left + 1 - maxF > k){
                count.set(s[left], count.get(s[left]) - 1);
                left++
            };

            res = Math.max(right - left + 1, res)
        }

        return res;
    }
}
