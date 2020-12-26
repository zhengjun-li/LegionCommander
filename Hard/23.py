# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        distance = 1
        k = len(lists)
        while distance < k:
            #print(f'Distance is: {distance}')
            for i in range(0, k - distance, distance * 2):
                #print(f'i = {i}')
                lists[i] = self.merge(lists[i], lists[i + distance])
            distance = distance * 2
        return lists[0]
    
    def merge(self, l1: ListNode, l2: ListNode):
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
