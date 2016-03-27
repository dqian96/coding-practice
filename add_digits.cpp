/*
Problem: Add digits
(https://leetcode.com/problems/add-digits/)

The digital root is the single-digit sum of the iterative process of adding
up all the digits of a non-negative integer. 

Let n be a non-negative integer with m digits. Let d be the digital root of n.
Theorem: The digital root of n is 
d = {
		9 if n mod 9 == 0 &&  n != 0,
		n mod 9 otherwise

	}

Let's look at d for some n according to the iterative process:
Let n = 0, d = 0
n = 1, d  = 1
...
n = 8, d = 8
n = 9, d = 9
n = 10,d = 1
...
n = 19, d = 1

It should be clear from the above that the digital root, from n > 0, is 
repeating in a cycle of 1-9. 

*/


#include <iostream>


using namespace std;

int addDigits(int num) {
    if (num % 9 == 0 && num != 0) {
        return 9;
    }
    return num % 9;
}


int main() {

}