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
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    addTwoNumbers(head1, head2) {
       const dummy = new ListNode(0);
       let curr = dummy;

       let carry = 0;
       while(head1 || head2 || carry){

        const v1 = head1 ? head1.val : 0;
        const v2 = head2 ? head2.val : 0;

        const res = v1 + v2 + carry;

        const digit = res % 10;
        curr.next = new ListNode(digit)
        carry = Math.floor( res / 10)

        curr  = curr.next
       
        head1 = head1 ? head1.next : null;
        head2 = head2 ? head2.next : null;
       }
    return dummy.next;
    }
}
