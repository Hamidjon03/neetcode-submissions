class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isSubsequence(s, t) {
        let left = 0;

        for(let right = 0; right < t.length; right++){
            if(s[left] === t[right]){
                left++;
            }
            if(left >= s.length) return true
        }
        return false;
    }
}
