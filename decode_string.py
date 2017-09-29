# Problem: Decode String
# (https://leetcode.com/problems/decode-string/description/)

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        i = 0
        while 1:
            if i >= len(s):
                return "".join(stack)
            if s[i].isdigit():
                start = i
                while s[i].isdigit():
                    i += 1
                num = s[start:i]
                stack.append(num)
                continue
            if s[i] == ']':
                word = []
                while stack[-1].isalpha():
                    word.append(stack[-1])
                    stack.pop()
                word.reverse()
                numTimes = int(stack[-1])
                stack.pop()
                word = word * numTimes
                stack.append("".join(word))
                i += 1
                continue
            if s[i] == '[':
                i += 1
                continue
            stack.append(s[i])
            i += 1
            