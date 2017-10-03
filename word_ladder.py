# Problem: Word Ladder
# (https://leetcode.com/problems/word-ladder/description/)

from collections import defaultdict

class Solution(object):
    def bfs(self, graph, root, target):
        s = set()
        numLevels = 1
        queue = [root]
        while len(queue) != 0:
            numLevels += 1    
            nextLevel = []
            for node in queue:
                for n in graph[node]:
                    if n in s:
                        continue
                    if n == target:
                        return numLevels
                    nextLevel.append(n)
                    s.add(n)
            queue = nextLevel
        return 0
        
    def isAdjacent(self, word1, word2):
        numDifferentChars = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                continue
            if numDifferentChars == 0:
                numDifferentChars += 1
            else:
                return False
        return True
            
    def ladderLength(self, beginWord, endWord, wordList):
        graph = defaultdict(list)
        for w in wordList:
            graph[w] = []
        graph[beginWord] = []
        
        wordList.append(beginWord)
        for w in wordList:
            wordArr = [c for c in w]
            for i in range(len(wordArr)):
                ogChar = wordArr[i]
                ogWord = "".join(wordArr)
                for j in range(ord('a'), ord('z') + 1):
                    if j == ord(ogChar):
                        continue
                    wordArr[i] = chr(j)
                    word = "".join(wordArr)
                    if word in graph.keys():
                        graph[ogWord].append(word)
                wordArr[i] = ogChar
                
        return self.bfs(graph, beginWord, endWord)
