/*
Problem: Move Zeroes
(https://leetcode.com/problems/move-zeroes/)

Essentially, iterate through the array (using a pointer) and swap numbers to the
leftmost avaliable space (another pointer). We don't shift zeroes as "they don't exist
/empty space." Every time we swap we increment the free space pointer as that
location is no longer a "free space." Everything to the right of the free space pointer
is "free space" and everything to the left is "unavaliable."

This process can be done using one single loop. However, using two loops might be faster
as for one single loop, we may have to set >= nums.size()-1-pointerToAZeroLocation 
indices to zero.

O(n) time and in place.
*/
#include <iostream>
#include <vector>
#include <string>

using namespace std;

void moveZeroes(vector<int>& nums) {
    int pointerToAZeroLocation = 0;
    for(int i = 0; i < nums.size(); i++ ) {
    	if (nums[i] != 0) {
    		nums[pointerToAZeroLocation++] = nums[i];
    	}
    }	
    for (int i = pointerToAZeroLocation; i < nums.size(); i++) {
    	nums[i] = 0;
    }
}

int main() {

}