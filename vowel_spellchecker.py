# Problem: Vowel Spellchecker
# (https://leetcode.com/problems/vowel-spellchecker/)

# Done as part of contest 117
# This was done very stupidly. Should have used smarter hashing/mapping instead of brute force.

from collections import defaultdict

class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        worddict = set(wordlist)
        lowercase_wordlist = defaultdict(lambda: float('inf'))
        for i, w in enumerate(wordlist):
            lowercase_wordlist[w.lower()] = min(lowercase_wordlist[w.lower()], i)
        print(lowercase_wordlist)
        answers = []

        for q in queries:
            if q in worddict:
                match = q
            else:
                match, _ = self.check(q, worddict, wordlist, lowercase_wordlist)
            if match != '':
                answers.append(match)
                continue

            curr = []
            match, _ = self.backtrack(curr, q, worddict, wordlist, lowercase_wordlist)
            answers.append(match)

        return answers

    def backtrack(self, curr, q, worddict, wordlist, lowercase_wordlist):
        vowels = {'a', 'e', 'i', 'o', 'u'}

        if len(curr) == len(q):
            match, idx = self.check(''.join(curr), worddict, wordlist, lowercase_wordlist)
            return match, idx

        curr_idx = len(curr)
        if q[curr_idx].lower() not in vowels:
            curr.append(q[curr_idx])
            match, idx = self.backtrack(curr, q, worddict, wordlist, lowercase_wordlist)
            curr.pop()
            return match, idx
        else:
            best_match, best_idx = '', float('inf')
            for v in vowels:
                curr.append(v)
                match, idx = self.backtrack(curr, q, worddict, wordlist, lowercase_wordlist)
                curr.pop()

                if idx < best_idx:
                    best_idx = idx
                    best_match = match

            return best_match, best_idx

    def check(self, q, worddict, wordlist, lowercase_wordlist):
        if q.lower() in lowercase_wordlist:
            idx = lowercase_wordlist[q.lower()]
            return wordlist[idx], idx
        return '', float('inf')
