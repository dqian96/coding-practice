# Problem: 3Sum
# (https://leetcode.com/problems/3sum/)

# Formalization:
# Let S = [s0, s1, s2, s3, ..., sn-1] be an array of n integers.
# Find all such unique (a, b, c) where a,b,c E S and a + b + c = 0.

# I will present two solutions.
# The first solution is to iterate through S, for possible values of a
# (i.e. for a in S) or in other words, "fix a" and try to find
# b and c satsifying a + b + c. 
# If a = si, then try to find matching b and c in [si+1,...,sn-1].
# How do we find these b's and c's? We can do this using two nested
# for loops or in another way... We make a hash table of
# the integers in S and the indicies that they occur in (i.e. (3, [1,2,3]))
# so we have O(1) lookup. Then we iterate through [si+1,...,sn-1]
# and fix each possible element in [si+1,...,sn-1] as b. So now we have
# a possible a,b pair. We can use c = -b - a in order to find c.
# We use the hash table to lookup the desired c. If c exists
# at an index following b (and therefore following a), then we add
# it to the solution set IF it not already in the solution set.
# We have to check the index to confirm it is an number that is not
# used as a or b. We use a set so that the result set only contains
# unique solutions. This is O(n^2)?

# The second solution is better.
# Ok first we sort the array.
# Then, we once again iterate through the array S and
# "fix" each element we come across as a.
# Now we seek the appropriate b and c's.
# Essentially, if a = si, then we are seeking a valid b and c
# in Ss = [si+1,...,sn-1]. Essentially, this problem reduces
# down to finding a two sum/pair b + c = -a in the sorted subarray
# Ss. Ok, now we will use a two pointers approach.
# Let p1 (symbolizing b) and p2 (symbolizing c) point to si+1 and 
# sn-1 respectively. If p1 + p2 > -a (i.e. invalid b and c), then
# we decrement p2. Since the array is SORTED left to right, this p2
# will be smaller than the previous, and so the p1 + p2 should be smaller.
# (i.e. closer to -1). We keep decrementing p2 until p1 + p2 <= -a.

# If p1 + p2 = -a, then great we found a + b + c = 0 triplet.
# Now, we INCREMENT p1. We know that all values to the left of p1
# combined with the values to the right of p2 > -a (too big).
# Now since p1 is even bigger, we know that since the previous, smaller
# values of p1 combined with prev values of p2 is too bigger, then
# the new, current, even bigger value of p1 (since the list is sorted)
# is also definitely too big - hence we don't have to try
# the previous values for the new value of p1 (candidate b).
# If p1 stays the same, we increment it again, since the triplet
# would be the same and we are looking for unique solutions.
# We decrement p2 since p1 is now bigger so the previous
# p1 + p2 = -a will not work.

# If p1 + p2 < -a, we cannot find valid b and c. We do the same thing as above, 
# except we do not decrement p2 at the end, since it might be valid
# for a bigger p1.

# The two pointer condition is the following:
# All values [s0,...,p1] have found any and all possible
# matching pairs in [p2,...,sn-1] and vice versa excluding p1 and p2.
# So when p1 => p2, then all matching pairs are found in the array.
# This is because all the matching pairs for the left have been
# found and all for the right. If both p1 and p2 point
# to the same element, the matching pair for it is not found
# yet but it cannot exist, since it can't match left or with right.
# The key is to note that when I am at p1, and the right values of p2
# are too big and the current value is too small, then a matching
# pair cannot be found since it's a sorted array. So when I increment p1,
# the values to the right of p2 are definitley too big for the now-bigger
# p1 since they were bigger for the old smaller p1, so I don't have to check
# it for this p1, and so on.

# We also don't have to keep track of triplets, since each reported
# pair are unique. This is because the array is sorted.
# If we report some (a, b, c), then there is only one order that
# we can report it in, namely a <= b <= c, since the array is sorted.
# Ok, so let's see. For a fixed a, if (a, b0, c0) is a triplet.
# then (a, b1, c1), another triplet must have b0 != b1, since
# we are incrementing p1 until it is different. Therefore, as b1 != b0,
# and a  is fixed, c1 != c0 and it is different. So the inner loop
# cannot produce any repeated triplets.
# Now let's look at the outer loop. Similarly, if if two a's 
# are the same, consecutively, we increment a further and ignore it.
# Ignoring it is fine, as all solutions with that a were already found.
# Now what if we arrive at an a that was a previous b. Well since, 
# this a must be larger than the last a's, then the a0 in the previous
# triplet cannot be in the new one and we cannot have a duplicate.

# First solution.
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """

#         # create dictionary of (int, [indices]) KVPS for O(1) lookup
#         intsAndTheirIndices = {}
#         """
#         {
#             1: [0,2,3],
#             2: [1,5,6]
#         }
#         """
#         for i in range(0, len(nums)):
#             if nums[i] not in intsAndTheirIndices:
#                 intsAndTheirIndices[nums[i]] = [i]
#             else:
#                 intsAndTheirIndices[nums[i]].append(i)

#         tripletSet = set()
#         res = []
#         for x in range(0, len(nums) - 2):
#             # find b and c
#             a = nums[x]
#             for y in range(x + 1, len(nums) - 1):
#                 b = nums[y]
#                 c = -a - b
#                 if c in intsAndTheirIndices:
#                     for index in intsAndTheirIndices[c]:
#                         if index > y:
#                             triplet = [a, b, c]
#                             triplet.sort()
#                             tripletTuple = (triplet[0], triplet[1], triplet[2])
#                             if tripletTuple not in tripletSet:
#                                 tripletSet.add(tripletTuple)
#                                 res.append(triplet)
#                             break
#         return res

# Second solution

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for a in range(0, len(nums)):
            if a != 0 and nums[a] == nums[a - 1]:
                a += 1
            else:
                b = a + 1
                c = len(nums) - 1
                while b < c:
                    if nums[b] + nums[c] > -nums[a]:
                        c -= 1
                    else:
                        if nums[b] + nums[c] == -nums[a]:
                            res.append([nums[a], nums[b], nums[c]])
                            c -= 1
                        oldb = b
                        while nums[b] == nums[oldb] and b < c:
                            b += 1
        return res
