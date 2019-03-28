# Given a sorted linked list, delete all duplicates
# such that each element appear only once.
#
# Example 1:
# Input: 1->1->2
# Output: 1->2
# Example 2:
# Input: 1->1->2->3->3
# Output: 1->2->3

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from  listNode import ListNode

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node=head
        while node and node.next:
            if node.val == node.next.val:
                node.next=node.next.next
            else:
                node=node.next

        return head


node=ListNode(1)
node.next=ListNode(1)
node.next.next=ListNode(1)
result = Solution().deleteDuplicates(node)
while result:
    print(result.val)
    result=result.next

