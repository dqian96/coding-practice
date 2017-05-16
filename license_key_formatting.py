# Problem: License Key Formatting
# (https://leetcode.com/problems/license-key-formatting/#/description)

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        stringNoDashes = [s.upper() for s in S if s != "-"]
        groups = []
        endEdge = len(stringNoDashes) - 1
        for i in range(len(stringNoDashes) - 1 - K, -2, -K):
            startEdge = i + 1
            groups.append(''.join(stringNoDashes[startEdge:endEdge + 1]))
            endEdge = i
        print endEdge
        if endEdge != -1:
            groups.append(''.join(stringNoDashes[:endEdge + 1]))
        groups.reverse()
        return '-'.join(groups)
            