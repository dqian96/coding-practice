# Problem: Linked List Cycle II
# (https://leetcode.com/problems/linked-list-cycle-ii/discuss/)

class Solution(object):
    def detectCycle(self, head):
        A = head
        if A is None: return None
        slow = A
        fast = A
        while 1:
            if fast == None:
                return None
            slow = slow.next
            fast = fast.next
            if fast == None:
                return None
            fast = fast.next
            
            if slow == fast:
                break
        entry = A
        while slow != entry:
            slow = slow.next
            entry = entry.next
        return entry
        