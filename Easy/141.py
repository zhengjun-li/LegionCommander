class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        nextNode = head.next
        while nextNode != None and nextNode != 'allo':
            prevNode = nextNode
            nextNode = nextNode.next
            prevNode.next = 'allo'
        if nextNode == None:
            return False
        elif nextNode == 'allo':
            return True