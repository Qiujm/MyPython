# Given a linked list, remove the n-th node from the end
# of list and return its head.
#
# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Follow up:
# Could you do this in one pass?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from  listNode import ListNode

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next :
            return
        slow=fast=head
        for i in range(n):
            fast=fast.next
        if not fast:
            head = head.next
            return head

        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head



node=ListNode(1)
node.next=ListNode(2)
result = Solution().removeNthFromEnd(node,2)
print(result.val)


