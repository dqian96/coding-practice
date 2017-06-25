# Problem: Implement Queue using Stacks
# (https://leetcode.com/problems/implement-queue-using-stacks/#/description)

# Use two stacks and dump it back and forth

class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.backFacingStack = []
        self.frontFacingStack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if self.frontFacingStack:
            self.dump(self.frontFacingStack, self.backFacingStack)
        self.backFacingStack.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.backFacingStack:
            self.dump(self.backFacingStack, self.frontFacingStack)
        return self.frontFacingStack.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.backFacingStack:
            self.dump(self.backFacingStack, self.frontFacingStack)
        return self.frontFacingStack[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.backFacingStack and not self.frontFacingStack
    
    def dump(self, sourceStack, targetStack):
        while sourceStack:
            targetStack.append(sourceStack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()