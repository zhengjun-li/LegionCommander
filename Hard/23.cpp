/** bigO = n lgk
 * works by divide and conquer similar to merge sort. Hardest part:
 * how do you write a while and for loop so that it merges the correct lists
 * in the right order!!!
 * 
 * start using nullptr over NULL
 * 
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {

        if(lists.empty())
        {
            return nullptr;
        }

        int k = lists.size();

        int distance = 1;

        while(distance < k)
        {
            cout << "k:" << k << endl;
            for(int i = 0; i < k - distance; i = i + (distance * 2))
            {
                cout << "i: " << i << endl;
                lists[i] = merge(lists[i], lists[i+distance]);
            }
            distance = distance * 2;
        }

        return lists[0];
      

    }

    ListNode* merge(ListNode* list1, ListNode* list2)
    {
        ListNode* it1 = list1;
        ListNode* it2 = list2;

        ListNode* head = new ListNode(0);
        ListNode* current = head;

        if(it1 == NULL)
        {
            return it2;
        }

        if(it2 == NULL)
        {
            return it1;
        }
        
        while(it1 != NULL && it2 != NULL)
        {
            if(it1->val <= it2->val)
            {
                current->next = it1;
                it1 = it1->next;
            }
            else
            {
                current->next = it2;
                it2 = it2->next;
            }
            current = current->next;
        }

        if(it1 == NULL)
        {
            current->next = it2;
        }
        else
        {
            current->next = it1;
        }
        return head->next;
    }
};