/*
Problem: Roman to Integer
(https://leetcode.com/problems/roman-to-integer/)

The crux of this problem is identifying patterns.
Going through several roman numeral examples, we notice the following patterns:

-The "digits" of the roman numerals and their respective integer mappings are:
	I:1
	V:5
	X:10
	L:50
	C:100
	D:500
	M:1000

	Seems that every power of 10 and every 5*a power of ten has its own digit

-Roman numerals are constructed by concatenations of these digits,
and the numerical value is simply the sum of the digits that were concatenated
e.g. VI = "V" + "I" = 5 + 1 = 6

-There are special cases. To represent any number that is a (roman numeral - "closest power 
of 10 to that numeral") to the roman numeral requires special positioning of the digits..
where the second digit - first digit = value
e.g. 450 = -100 + 500 + 50 = "C" + "D" + "L" = CDL

-For all "regular" numbers, the digit to the left is always >= than the digit 
to the right...e.g. XVIII = 10 + 5 + 1 + 1 + 1 = 18


Using the above information, we can construct the following method:
Using a hash table, create a mapping of the roman numerals to their integer value.
Iterate through the roman numeral, from left to right, and add the integer value of each 
numeral to a sum.
If the numeral is smaller than the one after it/left, we know that there's a special
condition, in which case we add the current numeral and subtract the next numeral and skip it.

This is a scalable, clean, easy-to-understand, short implementation (no cascading if's)
in O(n) time.

Once again, for "mathy" questions like this, it's wise to go about it in a
case-by-case scenario and look for PATTERNS.

*/

#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

int romanToInt(string s) {
	unordered_map<char, int> romanToIntgerMapping;
	romanToIntgerMapping['I'] = 1;
	romanToIntgerMapping['V'] = 5;
	romanToIntgerMapping['X'] = 10;
	romanToIntgerMapping['L'] = 50;
	romanToIntgerMapping['C'] = 100;
	romanToIntgerMapping['D'] = 500;
	romanToIntgerMapping['M'] = 1000;
	int sum = 0;
	for (int i = s.size() - 1; i >= 0 ; i--) {
		sum += romanToIntgerMapping[s[i]];
		if (romanToIntgerMapping[s[i-1]] < romanToIntgerMapping[s[i]] && i > 0) {
			sum -= romanToIntgerMapping[s[i-1]];
			i--;
		}
	}
	return sum;
}

int main() {}