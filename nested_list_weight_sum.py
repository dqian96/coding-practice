#   Problem: Nested List Weight Sum
#   (https://leetcode.com/problems/nested-list-weight-sum/)
#   SOLUTION: DFS

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        sum = 0
        listStack = [nestedList]
        indexStack = []
        index = -1;
        while len(listStack) != 0:
            # finished iterating list (pointer to one after last index)
            if index >= len(listStack[-1]) - 1:
                if len(listStack) == 1:
                    return sum
                index = indexStack[-1]
                listStack.pop()
                indexStack.pop()
                continue
            else:
                index += 1
            if listStack[-1][index].isInteger():
                sum += listStack[-1][index].getInteger()*len(listStack)
            else:
                listStack.append(listStack[-1][index].getList())
                indexStack.append(index)
                index = -1
        
                

        