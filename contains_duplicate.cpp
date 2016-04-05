/*
Problem: Contains Duplicate
(https://leetcode.com/problems/contains-duplicate/)

Simple problem. Iterate through the array, hashing every value. If collision, return
true.
*/


#include <vector>
#include <iostream>
#include <set>
using namespace std;

bool containsDuplicate(vector<int>& nums) {
	set<int> noDuplicate;
    for (int i = 0; i < nums.size(); i++) {
    	if (noDuplicate.count(nums[i]) != 0) return true;
    	noDuplicate.insert(nums[i]);
    }
    return false;
}

int main(){};

