/*
Problem: The Flip Game
(https://leetcode.com/problems/flip-game/)

Information given:
A string s of + or -, e.g. s = "++--+-+-"
You can flip any consecutive "++" into "--"
Possible states of s after one flip?

Information derived:
Seemingly random, no patterns. Hard to extract extra info. 
Have to look at every character or else no way of knowing - at least O(n) time
Relationship: If at any "+", the character before it is "+" then, we know it's a possible flip.
-> single pass through string and check whether or not there are consecutive "+"'s...
if there are, add it to the vector of possible states
*/

#include <vector>
#include <string>
#include <iostream>

using namespace std;

vector<string> generatePossibleNextMoves(string s) {
	vector<string> possibleStates;
	if (s.size() == 0 || s.size() == 1) return possibleStates;
    for (int i = 1; i < s.size(); i++) {
    	if (s[i-1] == '+' && s[i] == '+') {
    		s[i-1] = '-';
    		s[i] = '-';
    		possibleStates.push_back(s);
    	    s[i-1] = '+';
    		s[i] = '+';
    	}
    }
    return possibleStates;
}

int main() {
}