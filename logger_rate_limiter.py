# Problem: Logger Rate Limiter
#          (https://leetcode.com/problems/logger-rate-limiter/)

# Solution: We are given a tuple (message, timestamp), where message acts as the key
#           and the timestamp the value. Simply use a Python dictionary (hashmap) to record
#           the latest occurence in O(1). Lookup is O(1) for previous messages. Return true
#           depending on timestamp difference.


class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.records = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        
        if message in self.records:
            prevTimeStamp = self.records[message]
        else:
            prevTimeStamp = timestamp - 11

        if timestamp - prevTimeStamp >= 10:
            self.records[message] = timestamp
            return True            
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)