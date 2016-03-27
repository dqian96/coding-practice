/*
Problem: Palindrome Permutation
(https://leetcode.com/problems/palindrome-permutation/)

Given an n character string, there are n! permutations.
A naive solution would be to make a trie to represent all the possible permutations
and traverse it to find a palindrome.
i.e. To generate a trie, representing all the permutations of a string:
lettersLeft = ["a", "b", ... , ""]; //root is empty string
Node* generateTrie(vector<string> lettersLeft, int branchedOn) {
	Node* node = new Node();
	node->letter = lettersLeft.pop(branchedOn);
	for (int i = 0 ; i <  lettersLeft.size(); i++) {
		node->children.push_back(generateTrie(  lettersLeft, i ));
	}
	return node;
}
However, this is extremely computationally extensively - O(n!) time.

Let's if there is a better solution.

Palindromes can only come in 2 forms:
Even letters, with the first half having the same usage of characters as the second half.
It is readily apparent that if any letter l appears in the first half, it must
also appear in the 2nd half. Therefore, for the string to be palindromic, 
all letters must appear in multiples of 2.

Odd letters, with the 1st half == 2nd half but with a letter in between. 
Any letter l that appears in the string must appear in multiples of 2, except 1 letter
(being the middle 1).

We can use a set to keep track of letter occurences.
We pass through the string and record letter occurences to check if it's a palindrome.

This solution is O(n) time with n being the length of the string.
*/

#include <string>
#include <iostream>
using namespace std;

/*
bool canPermutePalindrome(string s) {
    set<char> letterOccurences;
    for (int i = 0; i < s.size(); i++) {
    	if (letterOccurences.count(s[i]) != 0) {
    		letterOccurences.erase(s[i]);
    	}
    	else {
    		letterOccurences.insert(s[i]);
    	}
    }
	return letterOccurences.size() == 0 || letterOccurences == 1;
}
*/

bool canPermutePalindrome(string s) {
	//using a bitset for better memory optimization
    bitset<25> letterOccurences (0);
    for (int i = 0; i < s.size(); i++) {
    		//a-z is 97 to 122, converting this to 0-25
  			letterOccurences[s[i] - 'a'] = !letterOccurences[s[i] - 'a'];
    }
   	return letterOccurences.count() == 0 || letterOccurences.count() == 1;
}
int main() {

}



