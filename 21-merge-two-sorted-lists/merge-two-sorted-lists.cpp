/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode head = ListNode(0);
        ListNode *cur = &head;
        ListNode *c1 = list1;
        ListNode *c2 = list2;
        while(c1 != NULL && c2 != NULL) {
            if(c1->val < c2->val) {
                cur->next = c1;
                c1 = c1->next;
            } else {
                cur->next = c2;
                c2 = c2->next;
            }
            cur = cur->next;
        }
        if(c1 == NULL) {
            cur->next = c2;
        } else {
            cur->next = c1;
        }
        return head.next;
    }
};