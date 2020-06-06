/** big O = longest input linked list size = n
 * iterates through both lists and just adds and carries over while creating new nodes
 * ++:
 * can be done with 1 while loop:
 *  condition is if carry exists or l1 or l2
 *  use if statements to get val from either list, and advance ptr1 and ptr2
 *      if list is empty, nothing will be grabbed and no iteration on that list
 *  add new node at the end
 * 
 * 
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if(l1 == NULL)
        {
            return l2;
        }
        if(l2 == NULL)
        {
            return l1;
        }

        ListNode* ptr1 = l1;
        ListNode* ptr2 = l2;
        ListNode* head;
        ListNode* tail;

        int carry = 0;
        int value = 0;

        value = ptr1->val + ptr2->val;
        if(value >= 10)
        {
            value = value % 10;
            carry = 1;
        }
        head = new ListNode(value);
        tail = head;
        ptr1 = ptr1->next;
        ptr2 = ptr2->next;

        while(ptr1 != NULL && ptr2 != NULL)
        {

            value = ptr1->val + ptr2->val + carry;
            cout << value << endl;
            carry = 0;
            if(value >= 10)
            {
                value = value % 10;
                carry = 1;
            }
            tail->next = new ListNode(value);
            tail = tail->next;
            ptr1 = ptr1->next;
            ptr2 = ptr2->next;
        }

        if(ptr1 == NULL)
        {
            while(ptr2 != NULL)
            {
                value = ptr2->val + carry;
                cout << value << endl;
                carry = 0;
                if(value >= 10)
                {
                    value = value % 10;
                    carry = 1;
                }
                tail->next = new ListNode(value);
                tail = tail->next;
                ptr2 = ptr2->next;
            }
        }
        else
        {
            while(ptr1 != NULL)
            {
                value = ptr1->val + carry;
                cout << value << endl;
                carry = 0;
                if(value >= 10)
                {
                    value = value % 10;
                    carry = 1;
                }
                tail->next = new ListNode(value);
                tail = tail->next;
                ptr1 = ptr1->next;
            }
        }
        
        if(carry == 1)
        {
            tail->next = new ListNode(carry);
            tail = tail->next;
        }
        return head;
    }
};