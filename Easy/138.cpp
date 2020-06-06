/*
bigO = n
very cool method of copying linked list with random pointers. 
think like dna strand/copying kind of, hard to explain
learned:
    DRAW OUT YOUR LINKED LIST OPERATIONS!!! FOR ALL
    


// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node* iterator = head;
        Node* nextNode;
        Node* deepCopy = NULL;

        while(iterator != NULL) //this adds a duplicate node that replaces the 'next' link
        {
            nextNode = iterator->next;
            Node* newNode = new Node(iterator->val);
            cout << "new node val:" << newNode->val << endl;
            iterator->next = newNode;
            newNode->next = nextNode;

            iterator = nextNode;
        }

        iterator = head;

        while(iterator != NULL)
        {
            if(iterator->random != NULL)
            {
                iterator->next->random = iterator->random->next;
            }

            iterator = iterator->next->next;
        }

        iterator = head;

        if(iterator != NULL)
        {
            deepCopy = iterator->next;
            nextNode = deepCopy;
            iterator->next = nextNode->next;
            iterator = iterator->next;
        }

        while(iterator != NULL)
        {
            cout << "here it: " << iterator->next->val << endl;
            nextNode->next = iterator->next;
            nextNode = iterator->next;
            iterator->next = iterator->next->next;
            iterator = iterator->next;
        }
        return deepCopy;
    }
};