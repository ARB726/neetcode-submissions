# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        firstList = list1
        secondList = list2
        dummyNode = ListNode()

        current = dummyNode
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2=list2.next
            else:
                current.next = list1
                list1=list1.next
            current = current.next
        
        if list1 and not list2:
            current.next=list1
        else:
            current.next=list2
        
        return dummyNode.next