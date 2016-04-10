/*
Problem: Majority Element
(https://leetcode.com/problems/majority-element/)

There are 2 implementations of the solution below. 

The first (commented out) method is the most straightfoward/intuitive way.
We iterate through the array, and count the number of occurences of each element
using a hashmap. We will eventually arrive at a count for a number that indicates
it is the majority element and we return it. 

The second method implements "Boyer–Moore majority vote algorithm," done in O(n)
time as well as, effectively, O(1) space.

This algorithm will find a majority algorithm if it exists. It will never indicate
the abscence of a majority element.

The intuition is as follows:

So: 
Let's assume M is the majority element of array A of size n.
Let Mc be the count of M, where Mc > floor(n/2) - hence the majority.
Let Nc be the count of of all other elements, hence Nc = floor(n/2).

We start by setting the elementToLookFor to the first element and the counter to 1.
As we iterate through the array, if the current element is the same as the elementToLookFor,
we increment the counter; if it is different, we decrement the counter.
Once the counter == 0, we set the elementToLookFor to the current element.

The elementToLookFor at the end of the iteration is the majority element,
provided that it exists.

We can see that "elements are fighting with each other." 
All elements of the same value will fight against all opposing elements
by lowering the counter but fight together with the same element
by increasing the counter.
The majority element is the element that occurs most, and is greater than the
cumulative sum of all other elements (Mc > Nc). This means that it will be able to decrement
the counters of all other elements to 0, and have at least 1 to its counter at the end 
of the iteration. 
Thus, the remaining element will always be the majority element.

*/

#include <unordered_map>
#include <vector>
#include <iostream>

/*
int majorityElement(vector<int>& nums) {
    unordered_map<int, int> count;
    if (nums.size() == 1) return nums[0];
    for (int i = 0; i < nums.size(); i++) {
    	if (count.count(nums[i]) == 0) {
    		count[nums[i]] = 1;
    	}
    	else {
    		count[nums[i]]++;
    		if (count[nums[i]] > nums.size()/2) {
    			return nums[i];
    		}
    	}
    }
}
*/

int majorityElement(vector<int>& nums) {
    int count = 1;
    int element = nums[0];
    for (int i = 1; i < nums.size(); i++) {
    	if (nums[i] == element) {
    		count++;
    	}
    	else {
    		count--;
    	}
    	if (count == 0) {
    		element = nums[i];
    		count = 1;
    	}
    }
    return element;
}


int main() {}