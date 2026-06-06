class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        // position = [4, 1, 0, 7] speed = [2, 2, 1, 1]
        let pair = position.map((item, idx) => [item, speed[idx]]);
        pair.sort((a, b) => b[0] - a[0]);
        
        let stack = [];

        for(let [p, s] of pair){
            stack.push((target - p)/s);
            if(stack.length >= 2 && stack[stack.length - 1] <= stack[stack.length - 2]){
                stack.pop()
            }
        }

        return stack.length;
    }
}
