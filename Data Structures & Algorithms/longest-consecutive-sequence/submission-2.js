class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
      let set = new Set(nums);
      let maxLong = 0;

      for(const num of nums){
        let length = 1;
        let nextNum = num + 1;
        while(set.has(nextNum)){
            nextNum++;
            length++;
        }
        maxLong = Math.max(length, maxLong)
      }

      return maxLong;
    }

}
