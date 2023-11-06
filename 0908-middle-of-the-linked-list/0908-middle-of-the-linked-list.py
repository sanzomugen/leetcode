# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        n = 0
        while curr_node:
            n+=1
            curr_node = curr_node.next
        count=0
        n=n//2+1
        curr_node = head
        while curr_node:
            count+=1
            if count==n:
                break
            curr_node=curr_node.next
        return curr_node


        