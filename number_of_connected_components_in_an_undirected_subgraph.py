# Number of Connected Components in an Undirected Graph
# (https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

class Solution(object):
    def dfs(self, edges, s, visited):
        while len(s) != 0:
            nodeToVisit = s[-1]
            s.pop()
            visited.add(nodeToVisit)
            for edge in edges[nodeToVisit]:
                if edge not in visited:
                    s.append(edge)
    
    def countComponents(self, n, edges):
        adjList = [[] for x in range(0, n)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
            
        visited = set()
        numComponents = 0
        for i in range(0, len(adjList)):
            if i not in visited:
                s = [i]
                self.dfs(adjList, s, visited)
                numComponents += 1
        return numComponents