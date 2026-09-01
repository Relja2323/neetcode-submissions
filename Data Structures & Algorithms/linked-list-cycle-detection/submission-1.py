# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(not head):
            return False
        spori = head
        brzi = head.next
        while(True):
            if(not brzi):
                return False
            elif(spori == brzi):
                return  True
            spori = spori.next
            brzi = brzi.next
            if(not brzi):
                return False
            brzi=brzi.next
