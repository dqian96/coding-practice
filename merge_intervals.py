# Problem: Merge intervals
# (https://leetcode.com/problems/merge-intervals/description/)

class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 0: return []
        intervals = sorted(intervals, key=lambda x: x.start)
        mergedIntervals = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i].start <= mergedIntervals[-1].end:
                mergedIntervals[-1].end = max(mergedIntervals[-1].end, intervals[i].end)
                continue
            mergedIntervals.append(intervals[i])
        
        return mergedIntervals
    