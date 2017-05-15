# Problem: Remove Linked List Elements
# (https://leetcode.com/problems/remove-linked-list-elements/#/description)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr != None:
            if curr.val == val:
                if head == curr:
                    head = curr.next
                else:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head