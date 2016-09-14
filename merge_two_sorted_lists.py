# Problem: Merge Two Sorted Lists
# (https://leetcode.com/problems/merge-two-sorted-lists/)

# We know that:
# a0 <= a1 <= a2 <= a3 <= a4 <= ... <= an and b0 <= b1 <= b2 <= b3 <= ... <= bk
# Assume m is a sorted, merged list composed of all a's and b's before i and j.
# Compare ai vs bj, starting from i = 0 and j = 0:
# WLOG If ai <= bj, then we know that ai is before bj, bj+1, bj+2, ... and ai+1, ai+2, ... in the sorted, merged list.
# Therefore, beforve moving forwards, we know that ai is at the end of the sorted, merged list:
# i.e. m = ..., ai
# Before appending ai, m is sorted.
# ai is the only correct choice to append.
# After appending ai, m is still merged and sorted. 
# Continue this process for ai+1 vs bj.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # fake head
        l3 = ListNode(1)
        temp = l3
        while (l1 != None and l2 != None):
        	if l1.val <= l2.val:
        		temp.next = ListNode(l1.val)
        		l1 = l1.next
        	else:
        		temp.next = ListNode(l2.val)
        		l2 = l2.next
        	temp = temp.next

        # add remaining
        if l1 != None:
        	temp.next = l1
        elif l2 != None:
        	temp.next = l2

        return l3.next