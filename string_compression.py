# Problem: String Compression
# (https://leetcode.com/problems/string-compression/description/)

class Solution(object):
    def write(self, chars, writerHead, c, count):
        chars[writerHead] = c
        writerHead += 1
        if count != 1:
            strCount = str(count)
            for c in strCount:
                chars[writerHead] = c
                writerHead += 1
        return writerHead

    def compress(self, chars):
        charCount = 1   # number of contiguous occurences of a character
        writerHead = 0  # position to start writing compressed array to next
        for i in range(1, len(chars) + 1):
            if i == len(chars) or chars[i] != chars[i - 1]:
                # end of streak - write compression
                writerHead = self.write(chars, writerHead, chars[i - 1], charCount)
                charCount = 1
            else:
                # ongoing streak
                charCount += 1
        return writerHead

