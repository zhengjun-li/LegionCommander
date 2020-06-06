/** bigO = n size of list
 *  maintain a gap of size n and iterate through the list. then just delete once forward node
 * hits the end of the list
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        if(head == NULL)
        {
            return head;
        }

        ListNode* tailIterator = head;
        ListNode* lagger = head;
        ListNode* deleteNode = head;

        for(int i = 1; i < n; i++)
        {
            tailIterator = tailIterator->next;
        }

        if(tailIterator->next == NULL)
        {
            head = head->next;
            return head;
        }

        tailIterator = tailIterator->next;
        deleteNode = deleteNode->next;
        lagger = head;

        while(iterator->next != NULL)
        {
            tailIterator = tailIterator->next;
            deleteNode = deleteNode->next;
            lagger = lagger->next;
        }

        lagger->next = deleteNode->next;
        return head;
    }
};