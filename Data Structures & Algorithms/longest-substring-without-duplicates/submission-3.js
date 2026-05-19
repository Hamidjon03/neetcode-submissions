class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        const n = s.length;
        let set = new Set();
        let left = 0;
        let right = 0;
        let longest = 0;
        while(right < n){
            if(set.has(s[right])){
                set.delete(s[left]);
                left++;
            } else{
                set.add(s[right]);
                longest = Math.max(longest, right - left + 1)
                right++;
            }
        }

        return longest;
    }
}
