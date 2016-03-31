/*
Problem: Shortest Word Distance
(https://leetcode.com/problems/shortest-word-distance/)

We are given an array of words, which may not be unique.
We are given words, a and b and must find the closest distance between the words.

The order/words in the array is random, bar that one word must occur before the other.
The closest possible distance is 1.

We must pass through the array at least once, O(n) time, and find the distance 
when word a/b occurs after b/a.
*/

#include <string>
#include <iostream>

using namespace std;

int shortestDistance(vector<string>& words, string word1, string word2) {
	int index1 = -1, index2 = -1, shortestDist = words.size();
    for (int i = 0; i < words.size(); i++) {
    	if (words[i] == word1) {
    		index1 = i;
    	}
    	else if (words[i] == word2) {
    		index2 = i;
    	}
    	if (abs(index1-index2) < shortestDist && index1 != -1 && index2 != -1) {
    		shortestDist = abs(index1-index2);
    		if (shortestDist == 1) return 1;
    	}
    }
    return shortestDist;
}

int main() {
}