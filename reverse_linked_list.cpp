/*
Problem: Reverse Linked List
(https://leetcode.com/problems/reverse-linked-list/)

Very simple problem.
*/

#include <iostream>

using namespace std;

//Definition for singly-linked list.
struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};


ListNode* reverseList(ListNode* head) {
    ListNode* prev = NULL;
    ListNode* current = head;
    ListNode* temp;
    while (current != NULL) {
        if (prev == NULL) {
            prev = current;
            current = current->next;
        }
        else {
            temp = current->next;
            current->next = prev;
            prev = current;
            current = temp;
        }
    }
    return prev;
}

int main() {}