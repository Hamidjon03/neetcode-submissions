/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
class Solution {
    /**
     * @param {ListNode} headA
     * @param {ListNode} headB
     * @return {ListNode}
     */
    getIntersectionNode(headA, headB) {
        let lA = headA;
        let lB = headB;

        while(lA !== lB){
            lA = lA ? lA.next : headB;
            lB = lB ? lB.next : headA;
        }

        return lA
    }
}
