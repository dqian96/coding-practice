# Problem: Group Shifted Strings
#(https://leetcode.com/problems/group-shifted-strings/)

# DETAILS:
# -each character of the string could be lexiographically shifted downwards
# -if one character is shifted by n, all characters are shifted by n
# -shifting a word produces a sequence/list of words that represents the
#   incremental character shifts
# -given an array, find all words that are in a common shift sequence


# FORMALIZE:
# Let s0 = c0c1c2c3...cn-1 be a string/word with n characters.
# Let si+1 be a shift of si, i = [0, 25] since the 26th shift will result in
# s0 again. 
# Let a shift be defined as:
# for all ck in si, ck = ck + 1 mod 26 lexiographically. In other words,
# a shift means that every single character of the string is lexiograhically
# incremented (allowing wrap arounds).
# A shift sequence is the sequence of possible shifts/state for any string s0.
# i.e. s0, s1, s2,..., s25

# Let two words be:
# w1 = a0a1a2a3....an-1
# w2 = b0b1b2b3...bn-1
# w1 and w2 are in the same sequence if and only if some shift of w2 is equal to w1.
# In other words, if b0 + k = a0, b1 + k = a1,..., bn-1 + k = an-1 for k shifts.
# Therefore, as long as the distance between each character of w1 and each corresponding
# of w2 are constant across all characters, then there is a shift.
# If there is not a constant difference, then the k-shift that would make b0 = a0 
# would not make b1 = a1 as the distance between b1 and a1 is too different.

# IMPLEMENTATION:
#