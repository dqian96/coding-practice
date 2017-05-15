# Problem: Intersection of two linked lists
# (https://leetcode.com/problems/intersection-of-two-linked-lists/#/description)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        currA = headA
        currB = headB
        lengthA = 1
        lengthB = 1
        while currA != None or currB != None:
            if currA != None:
                currA = currA.next
                lengthA += 1
            if currB != None:
                currB = currB.next
                lengthB += 1
        longerList = headA if lengthA >= lengthB else headB
        shorterList = headA if longerList == headB else headB
        for i in range(abs(lengthA - lengthB)):
            longerList = longerList.next
        while longerList != shorterList:
            longerList = longerList.next
            shorterList = shorterList.next
        return longerList
        