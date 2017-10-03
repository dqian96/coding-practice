# Problem: Multiply Strings
# (https://leetcode.com/problems/multiply-strings/description/)

class Solution(object):
    def multiplyByDigit(self, digit, num):
        if digit == 0:
            return [0]
        res = []
        carry = 0
        for i in range(len(num) - 1, -1, -1):
            product = int(num[i]) * digit + carry
            res.append(product % 10)
            carry = product/10
        if carry != 0:
            res.append(carry)
        res.reverse()
        return res
            
            
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        temp = num2
        num2 = num2 if len(num2) >= len(num1) else num1
        num1 = temp if len(temp) < len(num1) else num1 
        
        partialSums = []
        maxLength = 0
        for i in range(len(num1) - 1, -1 , -1):
            numZeroes = len(num1) - 1 - i;
            partialSums.append(self.multiplyByDigit(int(num1[i]), num2))
            for j in range(numZeroes):
                partialSums[-1].append(0)
            maxLength = max(maxLength, len(partialSums[-1]))
        
        res = []
        carry = 0
        for i in range(-1, -len(partialSums[-1]) - 1, -1):
            acc = carry
            for j in range(len(partialSums)):
                acc += partialSums[j][i] if abs(i) <= len(partialSums[j]) else 0
            res.append(str(acc % 10))
            carry = acc/10
        
        while carry != 0:
            res.append(str(carry % 10))
            carry = carry/10
        
        res.reverse()
        
        return "".join(res)        
        