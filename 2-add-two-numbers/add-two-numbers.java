/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode res = new ListNode();
        ListNode curRes = res;
        ListNode cur1 = l1;
        ListNode cur2 = l2;
        while(cur1 != null || cur2 != null) {
            int v1 = 0;
            int v2 = 0;
            if(cur1 != null) {
                v1 = cur1.val;
                cur1 = cur1.next;
            }
            if(cur2 != null) {
                v2 = cur2.val;
                cur2 = cur2.next;
            }
            int s = v1 + v2 + carry;
            ListNode newNode = new ListNode(s % 10);
            carry = s / 10;
            curRes.next = newNode;
            curRes = curRes.next;
        }
        if(carry > 0) {
            curRes.next = new ListNode(carry);
        }
        return res.next;
    }
}