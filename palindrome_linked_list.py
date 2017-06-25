# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        numNodes = 0
        curr = head
        while curr != None:
            numNodes += 1
            curr = curr.next
        curr = head
        currCount = 0
        prev = None
        while currCount < numNodes:
            if currCount >= numNodes/2:
                if prev == None:
                    prev = curr
                    curr = curr.next
                else:
                    tmp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = tmp
            else:
                curr = curr.next
            currCount += 1
        curr = prev
        while head != curr:
            if head.val != curr.val: return False
            head = head.next
            if head == curr:
                return True
            curr = curr.next
        return True
