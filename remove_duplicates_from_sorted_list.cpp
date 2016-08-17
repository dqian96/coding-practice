/*
Problem: Remove Duplicates from Sorted List
(https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

Given a sorted linked list, we need to remove duplicates.
To optimize our algorithm...we need to take in extra information from the question
description.

Here's the key points of consideration:
-Sorted list -> all duplicates will be next to subsequent nodes -> compare with nodes after current one
-Linked list -> no indices, have to traverse 1-by-1 from single entry point -> while loop

*/

#include <unordered_map>
#include <iostream>
#include <string>
using namespace std;


//Definition for singly-linked list.
struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};
 
ListNode* deleteDuplicates(ListNode* head) {
	ListNode* curr = head;
	while (curr != NULL) {
		if (curr->next == NULL) break;
		if (curr->val == curr->next->val) {
			ListNode* temp = curr->next;
			curr->next = curr->next->next;
			delete temp;
		}
		else {
			curr = curr->next;
		}
	}
	return head;
}



int main() {}