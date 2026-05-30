class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
      const numsSet = new Set(nums);
      let longest = 0;

      for(let num of nums){
        let curLong = 1;
        let prevNum = num - 1;
        if(!numsSet.has(prevNum)){
          while(numsSet.has(num + curLong)){
            curLong++;
          }
          longest = Math.max(curLong, longest);
        }
      }

      return longest;
    }
    
}
