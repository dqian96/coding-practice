/*
Problem: Strobogrammtic Number
(https://leetcode.com/problems/strobogrammatic-number/)

A number is strobogrammatic if it appears the same when flipped 180.
For problems like these, it's good to visualize several cases or the situation.
Let's see what information we can extract for this problem.

-What happens when we flip a number 180 degrees?
	Consider a number n = a b c d  where each letter is a digit
	After we flip it 180 degrees, we have
	nF = dF cF bF aF (where aF etc. means digit flipped)
	Consider the odd case as well:
	m = a b c d e
	mF = eF dF cF bF aF

	For the number to be strobogrammatic, then m and mF must appear visually
	the same...therefore, in terms of visual appearance:
	a = eF, b = dF, c = cF, d = bF, e = aF...

	Essentially, the ith digit must look the same as the number.size()-1-ith 
	flipped for i  = n/2. If a middle number exists, it must look the same as
	itself when reflected. 

	These are the constraints that we have to test to see whether or not
	the number is strobogrammatic.
-What do numbers look like when flipped?
	0 - 0 
	1 - 1
	2 - NO PAIR
	3 - NO PAIR
	4 - NO PAIR
	5 - NO PAIR
	6 - 9
	7 - NO PAIR
	8 - 8
	9 - 6
	Therefore, let the set of "trivial reflections" be:
	A = {0, 1, 8}
	Let the set of non-trivial reflections be:
	B = {(6,9), (9,6)}
*/

#include <unordered_map>
#include <iostream>
#include <string>
using namespace std;

bool isStrobogrammatic(string num) {
	//use hashmap to store the mappings of number:numberFlipped instead of using ifs
	unordered_map<char, char> numberAndItsFlippedCorrespondance {{'0','0'}, {'1','1'}, {'8','8'}, {'6','9'}, {'9','6'}};
	for (int i = 0; i < num.size()/2+1; i++) {
		if (num[i] != numberAndItsFlippedCorrespondance[num[num.size()-1-i]]) return false;
	}
	return true;
}

int main() {}