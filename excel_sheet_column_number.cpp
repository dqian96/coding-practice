/*
Problem: Excel Sheet Column Number
(https://leetcode.com/problems/excel-sheet-column-number/)

Example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

Essentially, Excel Sheet Column Titles are a system for counting.
We have the base cases: letters A-Z that map to a number from 1-26
Successive permutations of these letters represent increments.

Essentially, this is like a "base 26" system using 26 symbols, much like how 1's and 0's
are the symbols of counting for a binary system.

Since this is just another system of counting, the conversion to base-10 should be 
the same like other systems:
e.g.

AB in base 26 = 1*(26^1) + 2*(26^0)  = 28 in decimal

Similarly, ABC = 1*(26^2) + 2*(26^1) + 3*(26^0)
The A is achieved by 26*26 = 26^2 cycles (26 cycles of the second
digit, where each cycle of the 2nd digit is done by 26 cycles of the 
3rd). Likewise, the second digit of B means there has been 26*2 cycles of the 
third digit to get to B. 
*/


#include <string>
#include <iostream>
#include <math.h>

using namespace std;


int titleToNumber(string s) {
    int count = 0;
    for (int i = 0; i < s.size(); i++) {
    	count += pow(26,(s.size()-1-i))*(s[i]-'A'+1);
    }
    return count;
}


int main() {}