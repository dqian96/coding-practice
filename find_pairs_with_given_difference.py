# Problem: Find Pairs with Given Difference

"""
Given an array arr of distinct integers and a nonnegative integer k,
write a function findPairsWithGivenDifference that returns an array of all pairs [x,y]
in arr, such that x - y = k. If no such pairs exist, return an empty array.

Note: the order of the pairs in the output array doesn’t matter.

Solutions:

1. Two sum with hash table (O(n) time and space)
2. Sort and binary search (O(nlogn) time, O(1) space)
3. If the array is already sorted, O(n) time and O(1) space by index tracking and
only seacrhing the relevant part of the array
"""

def find_pairs_with_given_difference(arr, k):
  arr.sort()
  pairs = []
  floor = 1
  for n in arr:
    for cand in range(floor, len(arr)):
      if arr[cand] - n > k:
        break
      if arr[cand] - n == k:
        pairs.append([n, arr[cand]])
      floor += 1
  return pairs

