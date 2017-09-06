# Problem: String Similarity

"""

You're given a list of strings. For each string, you are to find a score.

The score is defined as follows:
For each suffix of string s, accumulate the length of the longest common prefix of the suffix
and s. That is the score.

Solution:

To calculate the score for each string, simply iterate through each suffix, and determine
the longest common prefix via a for loop. This is costly at O(n^2) and will time out.

A more efficient solution would be to use Aho Corasick.

"""

def stringSimilarity(inputs):
    res = []
    for input in inputs:
        score = 0
        l = len(input)
        for i in range(l - 1, -1, -1):
            if i == 0:
                score += l
                break
            for j in range(i, l):
                if input[j - i] == input[j]:
                    score += 1
                else:
                    break
        res.append(score)
    return res
