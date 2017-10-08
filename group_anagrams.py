# Problem: Group Anagrams
# (https://leetcode.com/problems/group-anagrams/description/)

from collections import defaultdict

class Solution(object):
    def hashFunction(self, s, primeMapping):
        acc = 1
        for c in s:
             acc *= primeMapping[c]
        return acc
    
    def havePrimeFactors(self, n, primesBeforeIt):
        for p in primesBeforeIt:
            if n % p == 0:
                return True
        return False
    
    def generatePrimeMapping(self):
        primes = [2]
        currNum = 3
        while len(primes) != 26:
            if not self.havePrimeFactors(currNum, primes):
                primes.append(currNum)
            currNum += 1
        primeMapping = defaultdict(int)
        for i in range(ord('a'), ord('z') + 1):
            primeMapping[chr(i)] = primes[i - ord('a')]
        return primeMapping
    
    def groupAnagrams(self, strs):
        primes = self.generatePrimeMapping()
        
        ht = defaultdict(list)
        for s in strs:
            ht[self.hashFunction(s, primes)].append(s)
        
        res = []
        for k in ht.keys():
            res.append(ht[k])
        return res
        