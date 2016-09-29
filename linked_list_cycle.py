# Problem: Linked List Cycle
# (https://leetcode.com/problems/linked-list-cycle/)

# Let's first define what a cycle is.
# Given a linked list l = n0,n1,n2,n3,...,ni,...
# A cycle exists iff ni == n0. 
# Naturally, a trivial solution to this problem would be to
# iterate through l and compare every node iterated 
# to previous nodes. If there is a duplicated node,
# then obviously there is a cycle.
# Assuming k distinct nodes, this will be O(k) time
# and O(k) space (using a hashmap)

# Can we do better?
# If we are able to change the linked list, then we can do better.
# Every node we iterate to, we change it's pointer to the HEAD NODE.
# If we iterate to a node that is the HEAD NODE, then there must be
# a CYCLE in the linked list that bites the head of the linkedlist
# or a node that we've already been to and messed with the .next pointer, and
# so we end up at HEAD...which should never be possible in a linked list.
# Since we arrive back at a node we already visited, a cycle must exist.
# On the other hand, if we keep iterating and do not see 
# that a cycle, and arrive at None, then we bever arrive at a node we've already
# been to before, and the linkedlist is simply a chain.
# This will ensure constant space and O(k) time.


# A cycle does not exist <=> one node has node.next == None



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        curr = head.next
        while curr is not None:
            if curr == head:
                return True
            temp = curr.next
            curr.next = head
            curr = temp
        return False