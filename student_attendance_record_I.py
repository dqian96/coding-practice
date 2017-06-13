# Problem: Student Attendance Record I
# (https://leetcode.com/problems/student-attendance-record-i/#/description)

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absentOnce = False
        for i, record in enumerate(s):
            if record == 'A':
                if absentOnce:
                    return False
                absentOnce = True
            elif record == 'L' and i >= 2 and s[i - 1] == 'L' and s[i - 2] == 'L':
                return False
        return True
                