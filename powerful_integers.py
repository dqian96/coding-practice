# Problem: Powerful Integers
# (https://leetcode.com/problems/powerful-integers/)

# Done as part of contest 118

from collections import defaultdict

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        cache = defaultdict()

        results = set()

        for i in range(100 + 1):
            if i == 0:
                curr_x = 1
            else:
                curr_x = curr_x * x
            if curr_x > bound: break

            for j in range(100 + 1):
                if j in cache:
                    curr_y = cache[j]
                elif j - 1 in cache:
                    curr_y = cache[j - 1] * y
                    cache[j] = curr_y
                else:
                    cache[0] = 1
                    curr_y = 1
                val = curr_y + curr_x
                if val > bound and val not in results: break
                results.add(val)

        return list(results)

