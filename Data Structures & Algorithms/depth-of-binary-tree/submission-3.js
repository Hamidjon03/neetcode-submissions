/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    maxDepth(root) {
        if(root === null) return 0;


        // DFS recursion
        // return (1 + Math.max(this.maxDepth(root.left), this.maxDepth(root.right)));

        // BFS
        let queue = [root];
        let depth = 0;
        
        while (queue.length > 0) {
            depth++; 
            let levelSize = queue.length; 
            
            for (let i = 0; i < levelSize; i++) {
                let currentNode = queue.shift();
                
                if (currentNode.left) queue.push(currentNode.left);
                if (currentNode.right) queue.push(currentNode.right);
            }
        }
        return depth;
        }
}
