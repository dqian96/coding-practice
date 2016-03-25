/*
Problem: Two sums
(https://leetcode.com/problems/two-sum/)

There is an extremely simple naive solution to the problem. The naive solution is to
do a nested for loop and compare each element with all the others to see which ones add up.

The solution detailed below incorporates the use of a hashtable to solve the problem
in O(n) time and O(n) space. The concept is that since the nums are given in an array
(ordered), one number of the solution set will occur before the other. As we pass
through the array, we lookup the hashtable for a previously scanned value that will 
satisfy "target". Since there is only one solution, the algorithm will keep scanning
the array until it arrives at the 2nd member of the solution set, and since an array
is ordered and there is only 1 solution, it will successfully look up the 1st member which
was added to the hashtable beforehand.
*/

#include <vector>
#include <string>
#include <iostream>
#include <unordered_map>
using namespace std;
vector<int> twoSum(vector<int>& nums, int target) {
	unordered_map<int, int> numsHashTable;
	vector<int> output;
    for (int i = 0; i < nums.size(); i++) {
    	if (numsHashTable.count(target -  nums[i]) != 0) {
    		output.push_back(i);
    		output.push_back(numsHashTable[target-nums[i]]);
    		return output;
    	}
		numsHashTable[nums[i]] = i;
    }
}		
int main() {
}