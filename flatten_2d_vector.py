# Problem: Flatten 2D Vector
# (https://leetcode.com/problems/flatten-2d-vector/description/)

class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        
        self.row = 0
        self.col = -1
        
        self.nextRow = -1
        self.nextCol = -1
        
        self.hasNext()  # sets to end if exits, otherwise finds next element
        
        # sets first element to iterator        
        self.row = self.nextRow
        self.col = self.nextCol
        
        
    def next(self):
        res = self.vec2d[self.row][self.col]
        
        self.row = self.nextRow
        self.col = self.nextCol
        
        return res
    
    def hasNext(self):
        if self.row == -1:
            return False
            
        for i in range(self.row, len(self.vec2d)):
            if len(self.vec2d[i]) == 0:
                continue
            if i != self.row:
                self.nextRow = i
                self.nextCol = 0
                return True
            else:
                if self.col + 1 == len(self.vec2d[i]):
                    self.nextCol = 0
                else:
                    self.nextCol = self.col + 1
                    self.nextRow = i
                    return True
                
        # end is the last iterator; one past last element
        self.nextRow = -1
        return True
            