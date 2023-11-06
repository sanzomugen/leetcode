# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_node = head
        fast_node = head
        while slow_node and fast_node.next:
            slow_node=slow_node.next
            fast_node = fast_node.next.next
            if fast_node is None:
                break
        return slow_node


        