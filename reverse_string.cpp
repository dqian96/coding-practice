/*
    RROBLEM: Reverse String
    (https://leetcode.com/problems/reverse-string/)

    SOLUTION: Use two pointers to swap the ith and size-1-ith letter, 
    for 0 <= i <= largestNumberSmallerThanMedian; 
    largestNumberSmallerThanMedian = (s.size() - 1.0)/2 - 0.2
    
    REASONING:
    Since C++ strings are MUTABLE (unlike Java strings) I use a two pointers to 
    swap the ith and the size-1-ith letter instead of reverse iteration and appending.
*/

#include <string>
#include <iostream>

std::string reverseString(std::string s) {
   int medianRoundedDown = (s.size() - 1.0)/2 - 0.2;
   for (int i = 0; i <= medianRoundedDown; i++) {
        std::swap(s[i], s[s.size()-1-i]);
   }
   return s;
}

int main() {
    std::cout << reverseString("test") << std::endl;
}