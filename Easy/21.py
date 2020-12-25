# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newListHead = ListNode()
        newList = newListHead
        attachNode = None
        current1 = l1
        current2 = l2
        while current1 != None and current2 != None:
            if current1.val <= current2.val:
                attachNode = current1
                current1 = current1.next
            else:
                attachNode = current2
                current2 = current2.next
            newList.next = attachNode
            newList = newList.next
        if current1 == None:
            newList.next = current2
        elif current2 == None:
            newList.next = current1
        return newListHead.next