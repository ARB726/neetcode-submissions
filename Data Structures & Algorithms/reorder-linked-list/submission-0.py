# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        
        fast = head.next

        while fast and fast.next :

            slow = slow.next

            fast = fast.next.next

# Now I know second linkedlist starts from slow.next (if odd second then second linked list will be short)

        secondPartOfLinkedList = slow.next
        prev = None
        slow.next = None

        while secondPartOfLinkedList:

            Next = secondPartOfLinkedList.next

            secondPartOfLinkedList.next = prev

            prev = secondPartOfLinkedList

            secondPartOfLinkedList = Next
        # print(prev)

# Now I know my second part of LinkedList is reversed

        firstHalf = head

        secondHalf = prev

        while secondHalf:

            tempfp = firstHalf.next # I am storing next point to avoid linkage broke (2)
 
            tempsp = secondHalf.next # I am store next point from second half of linked list to avoid linkage broke (3)

            firstHalf.next = secondHalf # 1->4 
            
            secondHalf.next = tempfp # 1-4-> 2

            firstHalf = tempfp 

            secondHalf = tempsp





"""

-> First Take fast pointer to the end of the list
-> Reverse the pointers after fast goes to the end so I mean second half
"""