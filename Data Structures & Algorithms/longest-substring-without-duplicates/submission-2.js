class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let set = new Set();
        let left = 0;
        let right = 0;
        let maxSize = 0;
        while(right < s.length){
            while(set.has(s[right])){
                set.delete(s[left]);
                left++;
            }

            set.add(s[right])
            right++;
            maxSize = Math.max(maxSize, set.size)
        }

        return maxSize
    }
}
