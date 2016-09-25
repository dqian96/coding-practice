# Problem: Add two numbers
# (https://leetcode.com/problems/add-two-numbers/)

# I will describe two ways to do this question.

# We could read in both numbers digit by digit and convert them
# to numbers first i.e. l1 = n0, n1, n2, ..., nk-1 => num(l1) = n0*1+n1*10+...+nk-1*10^k-1
# Then we add the numbers. After we add the numbers, we could use mod to fetch the digits,
# for example, num = d0d1d2d3...dn-1, di = num mod 10^(i+1).
# The time complexity is O(max(len(l1), len(l2))). However, we run the risk of overflow
# for large linked lists.

# This is a nother way to do it. add each corresponding node i in the two linked lists
# together, like a calculator. Don't forget the carry.
# We can do traverse both linked lists at the same time, in one loop, using
# conditionals to handle when one linked list is longer than the other.
# Essentially, we're mimicing a calculator. This is the same time complexity,
# but with no risk of overflow.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        temp = dummy
        carry = 0
        longerListCurrNode = None
        traversingLongerList = False
        while not (l1 is None and l2 is None) and not (traversingLongerList and longerListCurrNode is None):
            if not traversingLongerList and (l1 is None or l2 is None):
                traversingLongerList = True
                longerListCurrNode = l1 if l2 is None else l2
            if not traversingLongerList:
                value = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            else:
                value = longerListCurrNode.val + carry
                longerListCurrNode = longerListCurrNode.next
            carry = 1 if value > 9 else 0
            temp.next = ListNode(value % 10 if value > 9 else value)
            temp = temp.next
        if carry == 1:
            temp.next = ListNode(1)
        return dummy.next
