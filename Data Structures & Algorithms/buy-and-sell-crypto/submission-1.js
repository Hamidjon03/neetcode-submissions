class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        // lowPrice => low idx and low price
        // sellPrice => high idx and hight price
        // sellPrice idx > lowPrice idx && sellPrice > lowPrice

        let maxProfit = 0;
        let left = 0;

        for(let right = 1; right < prices.length; right++){
            if(prices[left] > prices[right]){
                left = right;
            } else {
                let curProfit = prices[right] - prices[left];
                maxProfit = Math.max(maxProfit, curProfit);
            }

        }
        return maxProfit;


    }
}
