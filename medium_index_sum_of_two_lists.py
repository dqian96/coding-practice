# Problem: Medium Index Sum of Two Lists
# (https://leetcode.com/problems/minimum-index-sum-of-two-lists/#/description)

from collections import defaultdict

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list1Lookup = defaultdict(str)
        for index, restaurant in enumerate(list1):
            list1Lookup[restaurant] = index
        score = float("inf")
        topRestaurants = []
        for index, restaurant in enumerate(list2):
            if restaurant not in list1Lookup:
                continue
            if index + list1Lookup[restaurant] < score:
                score = index + list1Lookup[restaurant]
                topRestaurants = [restaurant]
            elif index + list1Lookup[restaurant] == score:
                topRestaurants.append(restaurant)
        
        return topRestaurants
