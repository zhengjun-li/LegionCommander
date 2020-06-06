/**
 * bigO = total size of 2 lists
 * How to make better: once one list is empty, you can use attach rest of other list.
 * for initial empty list, use a code out side of while loop, makes it cleaner
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* ptr1 = l1;
        ListNode* ptr2 = l2;
        ListNode* tail = NULL;
        ListNode* head = NULL;
        int size = 0;
        while(ptr1 != NULL || ptr2 != NULL)
        {
            if(ptr1 == NULL && ptr2 != NULL)
            {
                if(size == 0)
                {
                    tail = ptr2;
                    ptr2 = ptr2->next;
                    tail->next = NULL;
                    head = tail;
                    size++;
                }
                else
                {
                    cout << "1" << endl;
                    tail->next = ptr2;
                    ptr2 = ptr2->next;
                    tail = tail->next;
                    tail->next = NULL;
                    size++;
                }
                continue;

            }
            if(ptr1 != NULL && ptr2 == NULL)
            {
                if(size == 0)
                {
                    tail = ptr1;
                    ptr1 = ptr1->next;
                    tail->next = NULL;
                    head = tail;
                    size++;
                }
                else
                {
                    cout << "2" << endl;
                    tail->next = ptr1;
                    ptr1 = ptr1->next;
                    tail = tail->next;
                    tail->next = NULL;
                    size++;
                }
                continue;
            }
            if(ptr1 != NULL && ptr2 != NULL)
            {

                if(ptr1->val <= ptr2->val)
                {
                        if(size == 0)
                    {
                        tail = ptr1;
                        ptr1 = ptr1->next;
                        tail->next = NULL;
                        head = tail;
                        size++;
                    }
                    else
                    {
                        cout << "2" << endl;
                        tail->next = ptr1;
                        ptr1 = ptr1->next;
                        tail = tail->next;
                        tail->next = NULL;
                        size++;
                    }
                    continue;
                }
                else
                {
                    if(size == 0)
                    {
                        tail = ptr2;
                        ptr2 = ptr2->next;
                        tail->next = NULL;
                        head = tail;
                        size++;
                    }
                    else
                    {
                        cout << "1" << endl;
                        tail->next = ptr2;
                        ptr2 = ptr2->next;
                        tail = tail->next;
                        tail->next = NULL;
                        size++;
                    }
                    continue;
                }
            }
        }
        return head;
    }
};