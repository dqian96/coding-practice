# Problem: Employee Information
# (https://leetcode.com/problems/employee-importance/description/)

from collections import defaultdict

class Solution(object):
    def findImportance(self, ht, employees, id):
        importance = employees[ht[id]].importance
        for e in employees[ht[id]].subordinates:
            importance += self.findImportance(ht, employees, e)
        return importance
            
    def getImportance(self, employees, id):
        ht = defaultdict(int)
        for i in range(len(employees)):
            ht[employees[i].id] = i
        
        return self.findImportance(ht, employees, id)
        