class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        let res = [];
        nums.sort((a,b) => a - b);

        for(let i = 0; i < nums.length; i++){
            if(nums[i] > 0) break;
            if( i > 0 && nums[i] === nums[i - 1]) continue;

            let right = nums.length - 1;
            let left = i + 1;

            while(left < right){
                const sum = nums[i] + nums[left] + nums[right];
                if(sum > 0){
                    right--;
                } else if(sum < 0){
                    left++;
                } else {
                    res.push([nums[i], nums[left], nums[right]]);
                    right--;
                    left++
                    while(left < right && nums[left] === nums[left -1]){
                        left++;
                    }
                }
            }
        }

        return res;        
    }
}
