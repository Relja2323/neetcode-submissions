# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(not list1 and not list2):
            return list1
        elif(not list1 and list2):
            return list2
        elif(list1 and not list2):
            return list1
        l1 = list1
        l2 = list2
        if l1.val > l2.val:
            tail = l2
            l2 = l2.next
        else:
            tail = l1
            l1 = l1.next
        dummy = tail
        while(l1 and l2):
            if l1.val > l2.val:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
            else:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
        while(l1):
            tail.next = l1
            tail = tail.next
            l1 = l1.next
        while(l2):
            tail.next = l2
            tail = tail.next
            l2 = l2.next
        return dummy
