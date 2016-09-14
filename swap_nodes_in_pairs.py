# Problem: Swap Nodes in Pairs
# (https://leetcode.com/problems/swap-nodes-in-pairs/)

# Let l = n0,n1,n2,n3,...,nk-1 be a linked list of k nodes
# After "swap nodes in pairs", s(l) = n1,n0,n2,n1,...,nk-2,nk-1 if k is even...
# If k is odd, then s(l) = n1,n0,n2,n1,...,nk
# Let's assume we are swapping nodes ni and ni+1. Then, we need to have a reference
# to ni-1 to swap them since the linked list is a "chain."
# Therefore, for a "head" ni-1, we need a 2x look ahead. We swap ni with ni+1 if both exist.
# Since ni and ni+1 are set (final order), we go to ni+1 as the "head." Keep going till end.
# Else, we don't swap.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # fake head so we don't have to do an extra case for the first node
        fakeHead = ListNode(None)
        fakeHead.next = head
        currNode = fakeHead

        # 2x look ahead condition
        while currNode.next != None and currNode.next.next != None:
        	temp = currNode.next
        	currNode.next = currNode.next.next
        	temp.next = currNode.next.next
        	currNode.next.next = temp
        	currNode = currNode.next.next
        	
        return fakeHead.next
