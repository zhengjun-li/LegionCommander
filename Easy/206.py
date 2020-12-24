# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #lets do this iteratively
        if head == None:
            return
        nodeList = [head]
        nextNode = head.next
        #put the linked list into a list of references to nodes
        while nextNode != None:
            nodeList.append(nextNode)
            nextNode = nextNode.next
            
        #iterate through the list reversed and modify 'next' attributes
        newHeadNode = nodeList[-1]
        currentNode = newHeadNode
        for node in reversed(nodeList):
            currentNode.next = node
            currentNode = node
        #this step is needed to break the loop
        currentNode.next = None
        return newHeadNode