/*
Problem: Valid Anagra
(https://leetcode.com/problems/valid-anagram/)

A very straightforward solution.
We begin by extracing the necessary information/patterns/definitions from 
the question.

An anagram is a word s where the letters of s can be used to construct t,
with no "extra letters."

So:

1. s and t must have the same length
2. s and t must have the same letters (type and occurence)

So, from this, we know that we can prove that s is an anagram of t
as long as the letter occurences are the same.

We have several solutions at our disposal:

1. Sort s and t, and compare. If s and t are anagrams, sorting them will get rid
of the difference due to order and put them in the same state. This might be 
computationally intensive as the length increases.

2. Iterate through s and t at the same time using a single loop (since same sizes),
and track the number of occurences using either a hash table/array. 
For occurences of s, we increment the count and for t, we can decrement the count,
if there are the same number of occurences of all the letters, the count will be 0/balanced for all 
letters at the end.

An array might be faster since, in c++, there is less overhead. 
But if UTF-8 letters are considered, a hash table would be better since the mapping
of letters to indicies would prove difficult using an array.

O(n) time, and O(1) space.
*/


#include <string>
#include <iostream>

using namespace std;

bool isAnagram(string s, string t) {
    if (s.size() != t.size()) return false;
    int numberOfLetterOccurences[26] = {0};
    for (int i = 0; i < s.size(); i++) {
    	if (s[i] == t[i]) continue;
    	numberOfLetterOccurences[s[i] - 'a']++;
    	numberOfLetterOccurences[t[i] - 'a']--;

    }
    for (int i = 0; i < 26; i++) {
    	if (numberOfLetterOccurences[i] != 0) return false;
    }
    return true;
}

int main() {};