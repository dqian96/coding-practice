# Problem: Kill Process
# (https://leetcode.com/problems/kill-process/#/description)

# This can be done without building the tree by recording the indices in the
# hash table.

from collections import defaultdict

class Solution(object):
    killList = []
    def collectNodes(self, pid, adjList):
        self.killList.append(pid)
        for child in adjList[pid]:
            self.collectNodes(child, adjList)
            
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        self.killList = []
        adjList = defaultdict(list)
        adjList[0] = []
        
        for i in range(len(pid)):
            adjList[ppid[i]].append(pid[i])
        
        self.collectNodes(kill, adjList)
        return self.killList
        