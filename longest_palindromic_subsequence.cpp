// Problem: Longest Palindromic Subsequence
// (https://leetcode.com/problems/longest-palindromic-subsequence/description/)

#include <string>
#include <iostream>

using namespace std;

void longestPalindromeSubseq(string s) {
    int n = s.size();
    
    // creating nxn table 
    int T[n][n];
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                T[i][j] = 1;  // base case, top L to bottom R longest (main) diagonal to 1's
            } else {
                T[i][j] = 0; // setting all other values to 0's
            }
        }
    }
    
    for (int i = 1; i < n; i++) {
        int l = 0;
        for (int r = i; r < n; r++) {
            // recursive case - fill table diagonally from top L to bottom R
            if (s[l] == s[r]) { // edges are the same - thus part of LPS
                T[l][r] = T[l+1][r-1] + 2;
            } else {    // edges aren't the same - check LPS with one edge removed
                T[l][r] = (T[l][r-1] > T[l+1][r]) ? T[l][r-1] : T[l+1][r];
            }
            l += 1;
        }
    }
    
    // results
    int longestLength = T[0][n - 1];
    string longestPalindrome = "";

    if (longestLength == 0) {
        cout << longestLength << endl;
        cout << longestPalindrome << endl;
        return;
    }
    
    // for filling in longestPalindrome
    int indexHelper = 0;
    
    for (int i = 0; i < longestLength; i++) {
        longestPalindrome += " ";   // initialize longestPalindrome with spaces
    }
    
    int l = 0;
    int r = n - 1;
    
    while (r > l) { // traversing the top right diagonal of table - stop when we get to the main top L to bottom R diagonal
        if (s[l] == s[r]) { // both edges are part of LPS
            longestPalindrome[indexHelper] = s[l];
            longestPalindrome[longestLength - 1 - indexHelper] = s[r];
            indexHelper += 1;
            l += 1; // move to immediate left-right diagonal in table
            r -= 1;
        } else { // one of the edges/none are in LPS
            if (T[l][r-1] >= T[l+1][r]) {
                r -= 1; // move left - favours smaller index
            } else {
                l += 1; // move down
            }
        }
    }
    if (l == r) {
        longestPalindrome[indexHelper] = s[l];  // if final position is on the main diag, add it to pali
    }
    
    cout << longestLength << endl;
    cout << longestPalindrome << endl;
}

int main() {
    longestPalindromeSubseq("ABCABC");
}